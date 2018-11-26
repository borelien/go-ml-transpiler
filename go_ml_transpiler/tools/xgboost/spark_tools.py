

def load_spark_model(model_path, metadata_path):

    import xgboost as xgb
    import json
    import numpy as np

    if not isinstance(model_path, str) or not isinstance(model_path, str):
        raise ValueError("model and metadata paths must be str, not {0} and {1}".format(type(model_path), type(metadata_path)))

    with open(metadata_path) as f:
        metadata = json.loads(f.read().strip())

    xgb_class = metadata.get("class")
    if xgb_class == "ml.dmlc.xgboost4j.scala.spark.XGBoostClassificationModel":
        clf = xgb.XGBClassifier()
        setattr(clf, "base_score", metadata["paramMap"]["baseScore"])
    elif xgb_class == "ml.dmlc.xgboost4j.scala.spark.XGBoostRegressionModel":
        clf = xgb.XGBRegressor()
    else:
        raise ValueError("Unsupported model.")

    setattr(clf, "objective", metadata["paramMap"]["objective"])
    setattr(clf, "missing",
            np.nan if metadata["paramMap"]["missing"] in ["NaN", "nan", "null", "None"] else metadata["paramMap"][
                "missing"])
    setattr(clf, "booster", metadata["paramMap"].get("booster", "gbtree"))
    setattr(clf, "n_estimators", metadata["paramMap"].get("numRound", 1))

    booster = xgb.Booster()
    booster.load_model(model_path)

    clf._Booster = booster
    return clf
