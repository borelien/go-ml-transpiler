package main

import (
	"testing"
	"google.golang.org/grpc"
	"context"
	"log"
	"math/rand"
	pb "github.com/znly/go-ml-transpiler/serving/proto"
)

func BenchmarkCall(b *testing.B) {

	b.StopTimer()
	conn, err := grpc.Dial("server:8080", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("Could not bind the grpc address.")
	}
	defer conn.Close()

	client := pb.NewModelClient(conn)
	ctx := context.Background()
	b.StartTimer()

	for n := 0; n < b.N; n++ {

		b.StopTimer()
		features := make([]float64, 30)
		for i := 0; i < len(features); i++ {
			features[i] = rand.Float64()
		}
		input := pb.ModelInput{Features: features}
		b.StartTimer()

		client.Forward(ctx, &input)
	}
}
