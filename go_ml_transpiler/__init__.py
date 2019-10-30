import os
import importlib


class Transpiler(object):

    def __init__(self, model):
        self.model = model
        self.type = type(self.model)
        self.model_name = self.type.__name__
        self.module = self.model.__module__.split(".")
        self.package_name = self.module[0]

        self.module_error = "Unsupported module: {}".format(".".join(self.module))

        local_module_path = [
            self.package_name,
            self.model_type,
            self.model_name]

        self.pwd = os.path.dirname(__file__)
        pckg = ".".join([os.path.split(self.pwd)[-1], "model"] + local_module_path)
        local_module = importlib.import_module(pckg)
        self._local_class = getattr(local_module, self.model_name)

    def transpile(
            self,
            package_name="model",
            export_method=True,
            method_name="predict",
            indent="    ",
            float_type="float64",
            **kwargs):
        self._local_class_instance = self._local_class(self.model, indent=indent, **kwargs)
        return self._local_class_instance.transpile(
            package_name=package_name,
            method_name=method_name,
            export_method=export_method,
            float_type=float_type,
            **kwargs)

    def write(self, directory):
        if not os.path.isabs(directory):
            directory = os.path.abspath(directory)
        self._local_class_instance.write(directory=directory)

    @property
    def model_type(self):
        if self.package_name == "xgboost":
            return self.xgb_model_type
        elif self.package_name == "sklearn":
            return self.sklearn_model_type
        raise ValueError(self.module_error)

    @property
    def xgb_model_type(self):
        if len(self.module) == 2:
            if self.module[1] == "sklearn":
                if self.type.__name__ == "XGBClassifier":
                    return "classifier"
                elif self.type.__name__ == "XGBRegressor":
                    return "regressor"
        raise ValueError(self.module_error)

    @property
    def sklearn_model_type(self):
        if len(self.module) == 3:
            if self.module[1] == "ensemble" and self.module[2] == "forest":
                if self.type.__name__ == "RandomForestClassifier":
                    return "classifier"
                elif self.type.__name__ == "RandomForestRegressor":
                    return "regressor"

        raise ValueError(self.module_error)
