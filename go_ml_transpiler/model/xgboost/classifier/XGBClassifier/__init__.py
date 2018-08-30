from go_ml_transpiler.model.xgboost.classifier import Classifier
from go_ml_transpiler.utils.model.xgboost import build_tree
import os


class XGBClassifier(Classifier):

    SUPPORTED_OBJECTIVE = [
        "reg:logistic",
        "binary:logistic",
        "binary:logitraw",
        "gpu:reg:logistic",
        "gpu:binary:logistic",
        "gpu:binary:logitraw",
        "multi:softprob",
        "multi:softmax",
    ]

    SUPPORTED_BOOSTER = [
        "gbtree",
        "dart",
    ]

    def __init__(self, model, indent, **kwargs):
        super(XGBClassifier, self).__init__(model=model, indent=indent, **kwargs)
        self._sanity_check()

    def transpile(self, package_name, method_name, export_method, **kwargs):

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
                    booster=build_tree(booster, indent=self.indent, missing_condition=self.missing_condition)
                )
            )
            booster_calls.append(
                "\n".join(
                    [
                        ("" if i == 0 else self.indent) + line
                        for i, line in enumerate(
                            self.template("{}_booster_call.template".format(
                                self.method_call_template_prefix)).format(
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
            "n_classes": self.num_classes,
            "n_boosters": self.num_boosters
        }
        if self.is_binary:
            k["base_score"] = self.model.base_score / (1. - self.model.base_score)

        method = self.template("{}_method.template".format(
            self.method_call_template_prefix)).format(**k)

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
