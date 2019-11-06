package main

import (
	"github.com/labstack/echo"
	"net/http"
)

func main() {
	a := 1
	bb := 2
	ccc := 3
	dddd := a + bb + ccc
	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		return c.String(http.StatusOK, "Hello World!"+string(dddd))
	})
	e.Logger.Fatal(e.Start(":1323"))
}
