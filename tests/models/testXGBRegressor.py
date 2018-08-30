from unittest import TestCase
from tests import TestPrediction
from xgboost import XGBRegressor


class XGBRegressorTest(TestPrediction, TestCase):

    predict_method = "predict"

    def _fit(self):
        self.models = [
            XGBRegressor(
                max_depth=7,
                n_estimators=10,
                learning_rate=0.1,
                n_jobs=-1,
                verbose=True,
                missing=-1,
                booster="dart",
                random_state=self.seed
            ).fit(self.x_test, self.regression_y_train),
            XGBRegressor(
                max_depth=20,
                n_estimators=20,
                learning_rate=0.01,
                n_jobs=-1,
                verbose=True,
                booster="gbtree",
                random_state=self.seed
            ).fit(self.x_test, self.regression_y_train)
        ]
