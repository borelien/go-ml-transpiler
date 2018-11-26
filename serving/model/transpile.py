import os
import xgboost as xgb
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.datasets import load_breast_cancer as load_dataset

from go_ml_transpiler import Transpiler

def main(export_dir):

    ## load dataset
    x, y = load_dataset(return_X_y=True)

    ## train xgb
    xgbc = xgb.XGBClassifier(n_estimators=100, max_depth=7)
    xgbc.fit(x, y)

    # transpile model
    os.mkdir(os.path.join(export_dir, "xgb"))
    transpiler = Transpiler(xgbc)
    transpiler.transpile(package_name="xgb", method_name="predict", export_method=True)
    transpiler.write(os.path.join(export_dir, "xgb"))
    print("xgb done.")


    ## train rfc
    rfc = RFC(n_estimators=100, max_depth=7)
    rfc.fit(x, y)

    # transpile model
    os.mkdir(os.path.join(export_dir, "rfc"))
    transpiler = Transpiler(rfc)
    transpiler.transpile(package_name="rfc", method_name="predict", export_method=True)
    transpiler.write(os.path.join(export_dir, "rfc"))
    print("rfc done.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("--export-dir", type=str)

    args = parser.parse_args()

    main(export_dir=args.export_dir)
