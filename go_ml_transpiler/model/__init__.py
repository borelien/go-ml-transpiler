import os


class Model(object):

    def __init__(self, model, model_type, indent, **kwargs):
        self.transpiled_model = None

        self.model = model
        self.indent = indent
        self.model_type = model_type

        self.module = self.model.__module__.split(".")
        self.package_name = self.module[0]
        self.model_name = type(self).__name__

        self._template = {}

        pwd = os.path.dirname(__file__)
        dirname = os.path.dirname(pwd)
        with open(os.path.join(dirname, "utils", "template", "import.template")) as f:
            self._template["import.template"] = f.read()

        local_module_path = [
            self.package_name,
            self.model_type,
            self.model_name]
        self.template_dir = os.path.join(pwd, *(local_module_path + ["templates"]))

    def template(self, t):
        if t not in self._template:

            try:
                with open(os.path.join(self.template_dir, t)) as f:
                    self._template[t] = f.read().replace("\t", self.indent)
            except:
                raise ValueError("{} cannot be found".format(t))

        return self._template.get(t)

    def transpile(self, **kwargs):
        raise NotImplementedError

    def write(self, directory):
        raise NotImplementedError
