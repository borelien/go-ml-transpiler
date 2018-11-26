# Serving Machine Learning using *gRPC* protocol


## Service

Here, we provide an "Hello world!" example of a machine learning serving service using `go-ml-transpiler`, *gRPC* and *Docker*.

To start the *Go* server:
```bash
$ make serving
```

Then, you can request the server using *gRPC*.

Here's a Python example:
```
$ python client/python/client.py
```

## Performance

We assess the performance of:
- the transpiled-model prediction latency
- the serving latency *via* *gRPC* request


Configuration:
```
Ensemble model: xgboost + random forest -> 100 estimators and max_depth=7
Dataset: Breast Cancer Wisconsin [1]

Model: MacBook Pro (15-inch, 2017)
Processor: Intel(R) Core(TM) i7-7920HQ CPU @ 3.10GHz
Memory: 16 GB 2133 MHz LPDDR3
```


Transpiled-model latency:
```bash
$ make benchmark_model
```

```
BenchmarkClassification-8   	  200000	      5486 ns/op
PASS
ok  	github.com/znly/go-ml-transpiler/serving/server	9.122ss
```


Serving latency:
```bash
$ make benchmark_api
```

```
BenchmarkCall-8   	    5000	    213446 ns/op
PASS
ok  	github.com/znly/go-ml-transpiler/serving/client	1.482s
```

To put this in perspective, the transpiled model is **~800 times faster** than in Python.

## References

[1] W. H. Wolberg, W. N. Street, O. L. Mangasarian ["Wisconsin Diagnostic Breast Cancer"](https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.names), 1995
