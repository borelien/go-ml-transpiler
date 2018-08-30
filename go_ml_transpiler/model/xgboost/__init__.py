from go_ml_transpiler.model import Model
import numpy as np


class XGBModel(Model):

    SUPPORTED_OBJECTIVE = {}
    SUPPORTED_BOOSTER = {}

    def __init__(self, model, indent, model_type, **kwargs):
        super(XGBModel, self).__init__(model=model, model_type=model_type, indent=indent, **kwargs)

        self.raw_boosters = self.model.get_booster().get_dump()
        self.n_estimators = self.model.n_estimators

        self.import_packages = []
        if np.isnan(self.model.missing):
            self.missing_condition = "math.IsNaN(features[{feature_index}])"
            self.import_packages.append("math")
        else:
            self.missing_condition = "features[{feature_index}]" + " == {value}".format(value=self.model.missing)

        self._objective_error = "Unsupported objective parameter: {}".format(self.model.objective)
        self._booster_error = "Unsupported booster type: {}".format(self.model.booster)
