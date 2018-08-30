package model

import (
    "math"
)


func Predict(features []float64) [2]float64 {
    sum := math.Log(9.000000000000002)
    sum += predict0(features)
    sum += predict1(features)
    sum += predict2(features)
    proba := 1.0 / (1.0 + math.Exp(sum))
    distribution := [2]float64{proba, 1.0 - proba}
    return distribution
}