package main

import (
	"google.golang.org/grpc"
	"context"
	pb "github.com/znly/go-ml-transpiler/serving/proto"
)


type Service struct {
	server *grpc.Server
	model  Model
}

func (s *Service) Forward(ctx context.Context, input *pb.ModelInput) (*pb.ModelOutput, error) {
	label, probability := s.model.classification(input.Features)
	output := &pb.ModelOutput{Label: label, Probability: probability}
	return output, nil
}
