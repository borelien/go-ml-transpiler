from go_ml_transpiler.model import Model


class ScikitLearnModel(Model):

    def __init__(self, model, indent, model_type, **kwargs):
        super(ScikitLearnModel, self).__init__(model=model, model_type=model_type, indent=indent, **kwargs)
        self.trees = self.model.estimators_
