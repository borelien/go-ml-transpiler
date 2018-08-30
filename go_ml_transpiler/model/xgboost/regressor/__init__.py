from go_ml_transpiler.model.xgboost import XGBModel


class Regressor(XGBModel):

    SUPPORTED_OBJECTIVE = ["reg:linear"]

    def __init__(self, model, indent, **kwargs):
        super(Regressor, self).__init__(model=model, model_type="regressor", indent=indent, **kwargs)
