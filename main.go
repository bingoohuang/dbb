package main

import (
	"database/sql"
	"fmt"
	_ "github.com/bingoohuang/dbb/dbi"
)

func main() {
	fmt.Printf("%+v\n", sql.Drivers())
}
