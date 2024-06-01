package main

import (
	"fmt"
	"net/http"
)

func main() {
	fmt.Println("Starting server...")
	mux := http.NewServeMux()

	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello World")
	})

	mux.HandleFunc("/comment", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Post a new comment")
	})

	if err := http.ListenAndServe("localhost:8080", mux); err != nil {
		panic(err)
	}
}
