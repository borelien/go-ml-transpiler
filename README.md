<p align="center">
	<img width=60% height=60% src="resources/pictures/go-ml-transpiler.png" alt="go-ml-transpiler"/>
</p>


# go-ml-transpiler


## Overview

`go-ml-transpiler` provides methods to export trained machine learning models as Go library, for large-scale applications with real-time constraints.


## Getting Started

### Supported models
| Algorithm | Training language |
| ------------- | ------------- |
| [**xgboost.XGBClassifier**](https://xgboost.readthedocs.io/en/latest/python/python_api.html) *(Scikit-Learn API only)* | Python |
| [**xgboost.XGBRegressor**](https://xgboost.readthedocs.io/en/latest/python/python_api.html) *(Scikit-Learn API only)* | Python |
| [**ml.dmlc.xgboost4j.scala.spark.XGBoostClassifier**](https://xgboost.readthedocs.io/en/latest/jvm/scaladocs/xgboost4j-spark/index.html#ml.dmlc.xgboost4j.scala.spark.XGBoostClassifier) | Scala/Spark |
| [**ml.dmlc.xgboost4j.scala.spark.XGBoostRegressor**](https://xgboost.readthedocs.io/en/latest/jvm/scaladocs/xgboost4j-spark/index.html#ml.dmlc.xgboost4j.scala.spark.XGBoostRegressor) | Scala/Spark |
| [**sklearn.ensemble.RandomForestClassifier**](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) | Python |
| [**sklearn.ensemble.RandomForestRegressor**](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html) | Python |


### Installation
```bash
$ git clone https://github.com/znly/go-ml-transpiler.git
$ cd go-ml-transpiler
$ pip install --user -e .
```


### Minimum requirements

```
- numpy
```


### Testing

```bash
$ make test
```

*Nota Bene:*

To run the tests on your machine, you will need [**go**](https://golang.org/) + these additional *Python* packages:
```bash
- xgboost
- scikit-learn
```


## Usage

### Serving
We provide a simple example of a machine learning serving service using `go-ml-transpiler`, *gRPC* and *Docker*.

- [code](https://github.com/znly/go-ml-transpiler/tree/master/serving) 🤖
- [blog](https://medium.com/p/5fece526b2ac) 🤓

### Transpile model
```python
from go_ml_transpiler import Transpiler
import xgboost
import numpy

# You can either load a picklized trained model:
# import pickle
# model = pickle.load(open("model.pickle", "rb"))
#
# Or train a fresh model:

Z = 15
N = 300
X = numpy.random.rand(N, Z)
Y = numpy.random.rand(N) > 0.5

model = xgboost.XGBClassifier(
        max_depth=7,
        n_estimators=10,
        learning_rate=0.1,
        n_jobs=-1,
        verbose=True,
        missing=-1,
        objective="reg:logistic",
        booster="dart",
        seed=0,
        base_score=0.9
    )

model.fit(X, Y)

transpiler = Transpiler(model=model)
transpiled_model = transpiler.transpile(
    package_name="model",
    export_method=True,
    method_name="Predict",
    indent="    ")
transpiler.write("/tmp")
```


### Leverage *Spark*
With *XGBoost* you can also train your model using *Spark* with the following few lines of code:
```scala
import org.apache.spark.ml.linalg.Vector
import ml.dmlc.xgboost4j.scala.spark.XGBoostClassifier

case class TrainingSample(
                   features: Vector,
                   label: Int
                 )

val SPARK_MODEL_DIR: String = ...

val dataset = Seq[TrainingSample](...).toDS()

val model = new XGBoostClassifier()
  .setFeaturesCol("features")
  .setLabelCol("label")
  .fit(dataset)

model.save(SPARK_MODEL_DIR)
```

Then, just load + transpile your model as previously:

```python
from go_ml_transpiler import Transpiler
from go_ml_transpiler.tools.xgboost.spark_tools import load_spark_model

model = load_spark_model(
    $SPARK_MODEL_DIR/data/$MODEL_FILE_NAME),
    $SPARK_MODEL_DIR)/metadata/$METADATA_FILE_NAME))

transpiler = Transpiler(model=model)
transpiled_model = transpiler.transpile()
transpiler.write($GOLANG_MODEL_DIR)
```


### Examples
When transpiling *XGBoost* models, output will look like this for the **booster** files:
```go
package model

func predict0(features []float64) float64 {
    if (features[0] < 0.5) || (features[0] == -1) {
        if (features[1] < 0.5) || (features[1] == -1) {
            if (features[7] < 0.941666901) || (features[7] == -1) {
                if (features[13] < 0.105796114) || (features[13] == -1) {
                    return -0.114391111
                } else {
                    (...)
```


with the following **prediction** API:
```go
package model

import (
    "math"
)

func Predict(features []float64) [2]float64 {
    sum := math.Log(9.0)
    sum += predict0(features)
    sum += predict1(features)
    sum += predict2(features)
    proba := 1.0 / (1.0 + math.Exp(sum))
    distribution := [2]float64{proba, 1.0 - proba}
    return distribution
}
```

*Nota Bene:*

Output is of type:
- [k]float64 for k-classes classification
- float64 for regression


## Authors

See [AUTHORS](./AUTHORS) for the list of contributors.


## References

[1] Gilbert Bernstein Morgan Dixon Amit Levy ["Faster Real-Time Classification Using Compilation"](https://courses.cs.washington.edu/courses/cse501/10au/compile-machlearn.pdf), 2010.


## License ![License](https://img.shields.io/badge/license-Apache2-blue.svg?style=plastic)

The Apache License version 2.0 (Apache2) - see [LICENSE](./LICENSE) for more details.

Copyright (c) 2018  Zenly   <hello@zen.ly> [@zenlyapp](https://twitter.com/zenlyapp)
