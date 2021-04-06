package main

import "fmt"

type iVehicle interface {
	setName(string)
	setPower(int)
	getName() string
	getPower() int
}

type vehicle struct {
	name  string
	power int
}

func (g *vehicle) setName(name string) {
	g.name = name
}

func (g *vehicle) getName() string {
	return g.name
}

func (g *vehicle) setPower(power int) {
	g.power = power
}

func (g *vehicle) getPower() int {
	return g.power
}

type linea struct {
	vehicle
}

func newLinea() iVehicle {
	return &linea{
		vehicle: vehicle{
			name:  "linea vehicle",
			power: 4,
		},
	}
}

type fusca struct {
	vehicle
}

func newFusca() iVehicle {
	return &fusca{
		vehicle: vehicle{
			name:  "fusca vehicle",
			power: 5,
		},
	}
}

func getVehicle(vehicleType string) (iVehicle, error) {
	if vehicleType == "linea" {
		return newLinea(), nil
	}
	if vehicleType == "fusca" {
		return newFusca(), nil
	}
	return nil, fmt.Errorf("Wrong vehicle type passed")
}

func main() {
	linea, _ := getVehicle("linea")
	fusca, _ := getVehicle("fusca")
	printDetails(linea)
	printDetails(fusca)
}

func printDetails(g iVehicle) {
	fmt.Printf("vehicle: %s", g.getName())
	fmt.Println()
	fmt.Printf("Power: %d", g.getPower())
	fmt.Println()
}
