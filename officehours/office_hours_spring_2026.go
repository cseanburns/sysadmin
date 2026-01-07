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

	fmt.Println("Today is:", weekday.String())

	switch weekday {
	case time.Wednesday:
		fmt.Println("Wednesday's office hours are 11AM - 1PM")
	case time.Thursday:
		fmt.Println("Thursday's office hours are 2:30PM - 4:30PM")
	default:
		fmt.Println("No office hours today.\nPlease scheduled an appt.")
	}
}
