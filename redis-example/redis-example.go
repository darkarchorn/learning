package main

import (
	"context"
	"encoding/json"
	"fmt"

	"github.com/go-redis/redis/v8"
	"github.com/google/uuid"
)

type Person struct {
	ID string
	Name       string `json:"name"`
	Age        int    `json:"age"`
	Occupation string `json:"occupation"`
}

func main() {
	fmt.Println("Starting server...")

	client := redis.NewClient(&redis.Options{
		Addr:     "localhost:6379",
		Password: "",
		DB:       0,
		// TLSConfig: &tls.Config{
		// 	InsecureSkipVerify: true,
		// 	MinVersion :tls.VersionTLS12,
		// },
	})

	ping, err := client.Ping(context.Background()).Result()
	if err != nil {
		panic(err)
	}
	fmt.Println(ping)

	err = client.Set(context.Background(), "name", "tphan", 0).Err()
	if err != nil {
		fmt.Printf("Failed to set value in the redis instance: %s", err.Error())
		return
	}

	name, err := client.Get(client.Context(), "name").Result()

	if err != nil {
		fmt.Printf("Failed to get value from redis instance: %s", err.Error())
		return
	}
	fmt.Println(name)

	tphanID := uuid.NewString()

	jsonString, err := json.Marshal(Person{
		ID: tphanID,
		Name: "Thang",
		Age: 22,
		Occupation: "Boss",
	}) 
	if err != nil {
		fmt.Printf("Failed to marshal: %s", err.Error())
		return
	}

	tphanKey := fmt.Sprintf("name : %s", tphanID)

	err = client.Set(context.Background(), tphanKey, jsonString, 0).Err()
	if err != nil {
		fmt.Printf("Failed to set value in the redis instance: %s", err.Error())
		return
	}
	person, err := client.Get(client.Context(), tphanKey).Result()

	if err != nil {
		fmt.Printf("Failed to get value from redis instance: %s", err.Error())
		return
	}

	print(person)
}
