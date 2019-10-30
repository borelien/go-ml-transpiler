from go_ml_transpiler.model.xgboost.regressor import Regressor
from go_ml_transpiler.utils.model.xgboost import build_tree
import os


class XGBRegressor(Regressor):

    SUPPORTED_OBJECTIVE = [
        "reg:linear"
    ]

    SUPPORTED_BOOSTER = [
        "gbtree",
        "dart",
    ]

    def __init__(self, model, indent, **kwargs):
        super(XGBRegressor, self).__init__(model=model, indent=indent, **kwargs)
        self._sanity_check()

    def transpile(self, package_name, method_name, export_method, float_type, **kwargs):

        low_method_name = method_name.lower()
        boosters = []
        booster_calls = []

        for i, booster in enumerate(self.raw_boosters):
            booster = booster.split()
            boosters.append(
                self.template("booster.template").format(
                    package_name=package_name,
                    import_packages=self.template("import.template").format(
                        packages="\n".join(
                            ['{0}"{1}"'.format(self.indent, package) for package in self.import_packages]))
                        if self.import_packages else "",
                    method_name=low_method_name,
                    method_index=i,
                    booster=build_tree(
                        booster,
                        indent=self.indent,
                        missing_condition=self.missing_condition,
                        float_type=float_type),
                    float_type=float_type
                )
            )
            booster_calls.append(
                "\n".join(
                    [
                        ("" if i == 0 else self.indent) + line
                        for i, line in enumerate(
                            self.template("booster_call.template").format(
                                method_name=low_method_name,
                                method_index=i
                            ).splitlines())
                    ]
                )
            )

        k = {
            "package_name": package_name,
            "method_name": method_name.capitalize() if export_method else method_name,
            "method_calls": "\n".join([("" if i == 0 else self.indent) + line for i, line in enumerate(booster_calls)]),
            "n_classes": 1,
            "base_score": float(self.model.base_score),
            "float_type": float_type
        }

        method = self.template("method.template").format(**k)

        self.transpiled_model = {"transpiled_model": {"boosters": boosters, "method": method}}
        return self.transpiled_model

    def write(self, directory):

        if self.transpiled_model is None:
            raise ValueError("You should first transpile the model")

        for i, booster in enumerate(self.transpiled_model["transpiled_model"]["boosters"]):
            with open(os.path.join(directory, "booster{}.go".format(i)), "w") as f:
                f.write(booster)

        with open(os.path.join(directory, "predict.go"), "w") as f:
            f.write(self.transpiled_model["transpiled_model"]["method"])

    def _sanity_check(self):

        if self.model.objective not in self.SUPPORTED_OBJECTIVE:
            raise ValueError("Unsupported objective: {}".format(self._objective_error))

        if self.model.booster not in self.SUPPORTED_BOOSTER:
            raise ValueError("Unsupported booster: {}".format(self._booster_error))
