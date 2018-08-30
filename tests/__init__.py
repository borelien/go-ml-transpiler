import subprocess
from go_ml_transpiler import Transpiler
import numpy as np
import os


class TestPrediction(object):

    # seed
    seed = 93659

    # train parameters
    Z = 15
    N = 100
    models = []

    # dataset
    prng = np.random.RandomState(seed)
    x_train = prng.rand(N, Z)
    x_test = prng.rand(N, Z)
    binary_class_y_train = prng.rand(N) > 0.5
    multi_class_y_train = (prng.rand(N) * 5).astype(int)
    regression_y_train = 10.0 * prng.rand(N)

    # i/o parameters
    test_directory = "tests"
    template_directory = os.path.join(test_directory, "templates")
    models_directory = os.path.join(test_directory, "models")
    tmp_directory = os.path.join(models_directory, "tmp")
    main = "./" + os.path.join(tmp_directory, "main")

    def setUp(self):
        subprocess.call(["rm", "-rf", self.tmp_directory])
        subprocess.call(["mkdir", self.tmp_directory])
        subprocess.call(
            [
                "cp",
                os.path.join(self.template_directory, "predict.template"),
                "{}.go".format(self.main)
            ]
        )

    def tearDown(self):
        subprocess.call(["rm", "-rf", self.tmp_directory])

    def _fit(self):
        pass

    def _transpile(self, model):
        transpiler = Transpiler(model=model)
        transpiler.transpile(
            package_name="main",
            export_method=True,
            method_name="Predict",
            indent="    ")
        transpiler.write(directory=self.tmp_directory)

    def _predict(self, model):
        subprocess.call(["go", "build", "-o", self.main, "./" + self.tmp_directory])
        self.original_prediction = model.__getattribute__(self.predict_method)(self.x_test)
        self.transpiled_prediction = np.squeeze(
            [
                [
                    float(v) for v in
                    subprocess.check_output([self.main] + [str(x) for x in sample], stderr=subprocess.STDOUT)
                    .decode("utf-8")
                    .replace("[","")
                    .replace("]","")
                    .split(" ")
                ]
                for sample in self.x_test
            ]
        )

    def test_predict(self):
        self._fit()
        for model in self.models:
            self._transpile(model=model)
            self._predict(model=model)
            np.testing.assert_array_almost_equal(self.original_prediction, self.transpiled_prediction, decimal=5)
