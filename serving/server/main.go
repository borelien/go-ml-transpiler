package main

import (
	"google.golang.org/grpc"
	"net"
	"flag"
	"log"
	"fmt"
	pb "github.com/znly/go-ml-transpiler/serving/proto"
)


var (
	Address = flag.String("p", ":8080", "Port")
)

func main() {

	fmt.Println("Starting server...")

	lis, err := net.Listen("tcp", *Address)
	if err != nil {
		log.Fatalf("Could not bind the grpc address.")
	}

	srv := Service{}
	srv.server = grpc.NewServer()

	pb.RegisterModelServer(srv.server, &Service{})
	srv.server.Serve(lis)
}
