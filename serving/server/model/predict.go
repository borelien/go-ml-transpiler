package model

import (
	"github.com/znly/go-ml-transpiler/serving/server/model/xgb"
	"github.com/znly/go-ml-transpiler/serving/server/model/rfc"
)

func Predict(features []float64) [2]float64 {

	distributionXGB := xgb.Predict(features)
	distributionRFC := rfc.Predict(features)

	return [2]float64{
		(distributionXGB[0] + distributionRFC[0]) / 2,
		(distributionXGB[1] + distributionRFC[1]) / 2,
	}
}
