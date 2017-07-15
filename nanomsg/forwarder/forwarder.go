package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"github.com/go-mangos/mangos"
	"github.com/go-mangos/mangos/protocol/pub"
	"github.com/go-mangos/mangos/protocol/sub"
	"github.com/go-mangos/mangos/transport/tcp"
	"io/ioutil"
	"os"
	"time"
)

// ConfigType represents config info
type ConfigType struct {
	PubURL string
	SubURL string
}

func die(format string, v ...interface{}) {
	fmt.Fprintln(os.Stderr, fmt.Sprintf(format, v...))
	os.Exit(1)
}

func date() string {
	return time.Now().Format(time.ANSIC)
}

func serve(pathname *string) {

	var msg []byte
	var err error
	var pubsock mangos.Socket
	var subsock mangos.Socket

	// read config File
	file, e := ioutil.ReadFile(*pathname)
	if e != nil {
		die("File error: %v", e)
	}
	fmt.Printf("config: %s\n", string(file))

	config := ConfigType{}
	json.Unmarshal(file, &config)

	if pubsock, err = pub.NewSocket(); err != nil {
		die("can't get new pub socket: %s", err)
	}
	pubsock.AddTransport(tcp.NewTransport())
	if err = pubsock.Listen(config.PubURL); err != nil {
		die("can't listen on pub socket: %s", err.Error())
	}

	if subsock, err = sub.NewSocket(); err != nil {
		die("can't get new sub socket: %s", err.Error())
	}
	subsock.AddTransport(tcp.NewTransport())
	if err = subsock.Listen(config.SubURL); err != nil {
		die("can't listen on sub socket: %s", err.Error())
	}
	// Empty byte array effectively subscribes to everything
	err = subsock.SetOption(mangos.OptionSubscribe, []byte(""))
	if err != nil {
		die("cannot subscribe: %s", err.Error())
	}

	fmt.Printf("%s: forwarder starts\n", date())
	for {
		if msg, err = subsock.Recv(); err != nil {
			die("Cannot recv: %s", err.Error())
		}
		fmt.Printf("%s: log: %s\n", date(), string(msg))

		if err = pubsock.Send(msg); err != nil {
			die("Failed publishing: %s", err.Error())
		}
	}
}

func main() {
	pathname := flag.String("config", "", "config pathname")
	flag.Parse()
	if *pathname == "" {
		die("%s --config <pathname>", os.Args[0])
	}
	serve(pathname)
}
