package model

func Predict(features []float64) float64 {
    prediction := 0.0
    prediction += predict0(features)
    prediction += predict1(features)
    prediction += predict2(features)
    return prediction
}
