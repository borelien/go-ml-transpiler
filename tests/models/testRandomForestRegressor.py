from unittest import TestCase
from tests import TestPrediction
from sklearn.ensemble import RandomForestRegressor


class RandomForestRegressorTest(TestPrediction, TestCase):

    predict_method = "predict"

    def _fit(self):
        self.models = [
            RandomForestRegressor(n_estimators=10, random_state=self.seed)
            .fit(self.x_test, self.regression_y_train)
        ]
