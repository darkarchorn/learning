package main

import (
	"context"
	"fmt"
	"time"
)

func enrichContext(ctx context.Context) context.Context {
	return context.WithValue(ctx, "request-id", "12345")
}

func doSomething(ctx context.Context) {
	rID := ctx.Value("request-id")
	fmt.Println(rID)
	for {
		select {
		case <-ctx.Done():
			fmt.Println("timed-out")
			return
		default:
			fmt.Println("do something cool")
		}
		time.Sleep(500 * time.Millisecond)
	}
}

func main() {
	fmt.Println("Go context")
	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Second)
	defer cancel()
	ctx = enrichContext(ctx)
	go doSomething(ctx)
	select {
	case <- ctx.Done():
		fmt.Println("deadline exceeded")
	}
	time.Sleep(2 * time.Second)
}

