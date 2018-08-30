from unittest import TestCase
from tests import TestPrediction
from xgboost import XGBClassifier


class XGBClassifierTest(TestPrediction, TestCase):

    predict_method = "predict_proba"

    def _fit(self):
        self.models = [
            XGBClassifier(
                max_depth=7,
                n_estimators=10,
                learning_rate=0.1,
                n_jobs=-1,
                verbose=True,
                missing=-1,
                booster="dart",
                base_score=0.9,
                random_state=self.seed
            ).fit(self.x_test, self.binary_class_y_train),
            XGBClassifier(
                max_depth=20,
                n_estimators=20,
                learning_rate=0.01,
                n_jobs=-1,
                verbose=True,
                booster="gbtree",
                random_state=self.seed
            ).fit(self.x_test, self.multi_class_y_train)
        ]
