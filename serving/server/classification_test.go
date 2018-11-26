package main

import (
	"testing"
	"math/rand"
)

func BenchmarkClassification(b *testing.B) {

	b.StopTimer()
	m := Model{}
	b.StartTimer()

	for n := 0; n < b.N; n++ {

		b.StopTimer()
		features := make([]float64, 30)
		for i := range features {
			features[i] = rand.Float64()
		}
		b.StartTimer()

		m.classification(features)
	}
}
