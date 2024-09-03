package main

import (
	"fmt"
	"reflect"
)

func main() {
	fmt.Println("Hello, World!")
	longDeclaration()
	typeInference()
	shortDeclaration()
	legalDeclaration()
	multipleDeclaration()
}

func longDeclaration() {
	var age int
	fmt.Println(age) // age initialized 0
	age = 30
	var age2 int = 30
	var a, b, c int = 1, 2, 3
	fmt.Println(age2, a, b, c)
}

func typeInference() {
	var number = 3000
	var string = "asdf"
	fmt.Println(reflect.TypeOf(number))
	fmt.Println(reflect.TypeOf(string))
}

func shortDeclaration() {
	bar := 30
	println(bar) //embedded function, it can be removed. use debug only?
	a := 10
	a, b := 20, 30
	println(a, b)
}

// global variable doesn't influence
// because foo here is scoped to some func
var foo int = 34

func legalDeclaration() {
	foo := 42 // <-- legal
	fmt.Println(foo)
	foo = 314 // <-- legal
	fmt.Println(foo)
}

func multipleDeclaration() {
	var (
		variable_first                  int
		variable_second, variable_third = 1, 4.5e9
		string_text                     = "hi"
	)
	println(variable_first)
	println(variable_second, variable_third)
	println(string_text)
}