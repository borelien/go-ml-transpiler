from go_ml_transpiler.model.xgboost import XGBModel


class Classifier(XGBModel):

    def __init__(self, model, indent, **kwargs):
        super(Classifier, self).__init__(model=model, model_type="classifier", indent=indent, **kwargs)
        self.num_boosters = len(self.raw_boosters)

        mod = divmod(self.num_boosters, self.n_estimators)[1]
        if mod != 0:
            raise ValueError(
                "Modulo(number of boosters, number of estimators) should be 0, here: {}".format(
                    self.num_boosters,
                    self.n_estimators,
                    mod))

        self.is_binary = self.num_boosters == self.n_estimators
        self.num_classes = 2 if self.is_binary else int(self.num_boosters / self.n_estimators)
        self.method_call_template_prefix = "binary" if self.is_binary else "multi"
