#!/bin/bash

## December 2018

## Todo: Offer to play the game again
## Todo: Keep score history

red=$(tput setaf 1)
green=$(tput setaf 2)
blue=$(tput setaf 4)
end=$(tput sgr0)

x=$((1 + RANDOM % 100))

clear
printf "Guess a number between 1 and 100.\n"
printf "What is your guess? "
read guess

if [[ "$guess" -eq "$x" ]] ; then
	printf "%s\n" "${blue}Are you psychic, because you guessed right away!${end}"
	exit 0
fi

until [[ "$guess" -eq "$x" ]]
do
if [[ "$guess" -gt "$x" ]] ; then
  printf "%s\n" "${red}Your guess is too high.${end}"
  read guess
  if [[ "$guess" -eq "$x" ]] ; then
    printf "%s\n" "${blue}Congratulations! $guess is correct!${end}"
  fi
elif [[ "$guess" -lt "$x" ]] ; then
  printf "%s\n" "${green}Your guess is too low.${end}"
  read guess
  if [[ "$guess" -eq "$x" ]] ; then
    printf "%s\n" "${blue}Congratulations! $guess is correct!${end}"
  fi
fi
done
