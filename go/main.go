package main

import (
	"fmt"
	"github.com/dgrijalva/jwt-go"
	"time"
)

type jwtCustomClaims struct {
	Name  string `json:"name"`
	Admin bool   `json:"admin"`
	jwt.StandardClaims
}

func main() {
	claims := &jwtCustomClaims{
		"test",
		true,
		jwt.StandardClaims{
			ExpiresAt: time.Now().Add(time.Minute * 30).Unix(), //有効期限を有効にしておく
		},
	}
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	// Secretで文字列にする. このSecretはサーバだけが知っている
	tokenstring, _ := token.SignedString([]byte("secret"))

	fmt.Println(tokenstring)
}
