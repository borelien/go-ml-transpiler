from unittest import TestCase
from tests import TestPrediction
from sklearn.ensemble import RandomForestClassifier


class RandomForestClassifierTest(TestPrediction, TestCase):

    predict_method = "predict_proba"

    def _fit(self):
        self.models = [
            RandomForestClassifier(n_estimators=10, random_state=self.seed)
            .fit(self.x_test, self.binary_class_y_train),
            RandomForestClassifier(n_estimators=10, random_state=self.seed, class_weight={1: 2.3, 0: 0.2})
            .fit(self.x_test, self.binary_class_y_train),
            RandomForestClassifier(n_estimators=10, random_state=self.seed)
            .fit(self.x_test, self.multi_class_y_train)
        ]
