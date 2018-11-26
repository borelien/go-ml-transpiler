package main

import "github.com/znly/go-ml-transpiler/serving/server/model"

type Model struct {
}

func (m *Model) classification(features []float64) (int64, float64) {
	distribution := model.Predict(features)
	label := 0
	probability := 0.0
	for i, v := range distribution {
		if v > probability {
			label = i
			probability = v
		}
	}
	return int64(label), probability
}
