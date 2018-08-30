from go_ml_transpiler.model.sklearn import ScikitLearnModel


class Classifier(ScikitLearnModel):

    def __init__(self, model, indent, **kwargs):
        super(Classifier, self).__init__(model=model, model_type="classifier", indent=indent, **kwargs)
