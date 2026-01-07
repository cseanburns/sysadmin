package main
import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("C. Sean Burns, PhD")
	fmt.Println("Associate Professor")
	fmt.Println("sean.burns@uky.edu\n")
	fmt.Println("Office Hours, Spring 2026\n")

	currentTime := time.Now()
	weekday := currentTime.Weekday()

	// alternate way using 'printf':
	// fmt.Printf("Now: %s\n", weekday)

	fmt.Println("Today is:", weekday.String())

	if (int(weekday)) == 3 {
		fmt.Println("Wednesday's office hours are 11AM - 1PM")
	} else if (int(weekday)) == 4 {
		fmt.Println("Thursday's office hours are 1PM - 3PM")
	} else {
		fmt.Println("No office hours today.\nPlease scheduled an appt.")
	}
}
