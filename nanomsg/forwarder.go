package main

import (
	"fmt"
	"github.com/op/go-nanomsg"
	"time"
)

var pubAddress = "tcp://127.0.0.1:5555"
var subAddress = "tcp://127.0.0.1:5565"

func serve() {
	var err error
	var pub *nanomsg.PubSocket
	var sub *nanomsg.SubSocket

	if pub, err = nanomsg.NewPubSocket(); err != nil {
		panic(err)
	}
	if _, err = pub.Bind(pubAddress); err != nil {
		panic(err)
	}

	if sub, err = nanomsg.NewSubSocket(); err != nil {
		panic(err)
	}
	if err = sub.Subscribe(""); err != nil {
		panic(err)
	}
	if _, err = sub.Connect(subAddress); err != nil {
		panic(err)
	}

	time.Sleep(10 * time.Millisecond)

	//var msg string
	fmt.Println("forwarder")
	for {
		msg, err := sub.Recv(0)
		if err == nil {
			fmt.Println("forwarder log:", msg)
			_, err2 := pub.Send(msg, 0)
			if err2 != nil {
				fmt.Println(err2)
			}
		} else {
			fmt.Println(err)
		}
	}
}

func main() {
	serve()
}
