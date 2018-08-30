from go_ml_transpiler.model.sklearn import ScikitLearnModel


class Regressor(ScikitLearnModel):

    def __init__(self, model, indent, **kwargs):
        super(Regressor, self).__init__(model=model, model_type="regressor", indent=indent, **kwargs)
