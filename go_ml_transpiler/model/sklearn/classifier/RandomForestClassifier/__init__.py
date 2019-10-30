from go_ml_transpiler.model.sklearn.classifier import Classifier
from go_ml_transpiler.utils.model.sklearn import build_tree
import os


class RandomForestClassifier(Classifier):

    def __init__(self, model, indent, **kwargs):
        super(RandomForestClassifier, self).__init__(model=model, indent=indent, **kwargs)
        self.num_classes = self.model.n_classes_

    def transpile(self, package_name, method_name, export_method, float_type, **kwargs):

        low_method_name = method_name.lower()
        trees = []
        tree_calls = []

        for i, tree in enumerate(self.trees):
            trees.append(
                self.template("tree.template").format(
                    package_name=package_name,
                    method_name=low_method_name,
                    method_index=i,
                    tree=build_tree(
                        left_nodes=tree.tree_.children_left.tolist(),
                        right_nodes=tree.tree_.children_right.tolist(),
                        thresholds=tree.tree_.threshold.tolist(),
                        values=tree.tree_.value.tolist(),
                        features=tree.tree_.feature,
                        indent=self.indent,
                        float_type=float_type,
                    ),
                    n_classes=self.num_classes,
                    float_type=float_type
                )
            )
            tree_calls.append(
                "\n".join(
                    [
                        ("" if i == 0 else self.indent) + line
                        for i, line in enumerate(self.template("tree_call.template").format(
                            method_name=low_method_name,
                            method_index=i
                        ).splitlines())
                    ]
                )
            )

        k = {
            "package_name": package_name,
            "method_name": method_name.capitalize() if export_method else method_name,
            "method_calls": "\n".join([("" if i == 0 else self.indent) + line for i, line in enumerate(tree_calls)]),
            "n_classes": self.num_classes,
            "float_type": float_type
        }

        method = self.template("method.template").format(**k)

        self.transpiled_model = {"transpiled_model": {"trees": trees, "method": method}}
        return self.transpiled_model

    def write(self, directory):

        if self.transpiled_model is None:
            raise ValueError("You should first transpile the model")

        for i, tree in enumerate(self.transpiled_model["transpiled_model"]["trees"]):
            with open(os.path.join(directory, "tree{}.go".format(i)), "w") as f:
                f.write(tree)

        with open(os.path.join(directory, "predict.go"), "w") as f:
            f.write(self.transpiled_model["transpiled_model"]["method"])
