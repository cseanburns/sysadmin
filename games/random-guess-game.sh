#!/bin/bash

# Random Number Guessing Game
# by Sean Burns
# Guess a number between 1 and 100
# Date: Tue 04 Dec 2018 
##
# Todo: 
# Ask players if they want to play again
# Track score history
# Tell players how many guesses it took to get the correct guess
# Generate a plot (gnuplot maybe?) plotting each random number as they play

red=$(tput setaf 1)
green=$(tput setaf 2)
blue=$(tput setaf 4)
end=$(tput sgr0)

x=$((1 + RANDOM % 100))

clear
#echo $x (uncomment to check if working)
printf "Guess a number between 1 and 100.\n"
printf "What is your guess? "
declare -i guess
read -r guess

if [[ $guess -eq $x ]] ; then
  printf "%s\n" "${blue}Are you psychic, because you guessed right away!${end}"
  exit 0
fi

until [[ $guess -eq $x ]]
do
  if [[ $guess -gt $x ]] ; then
    printf "%s\n" "${red}Your guess is too high.${end}"
    printf "Guess again: " ; declare -i guess ; read -r guess
    if [[ $guess -eq $x ]] ; then
      printf "%s\n" "${blue}Congratulations! $guess is correct!${end}"
    fi
  elif [[ $guess -lt $x ]] ; then
    printf "%s\n" "${green}Your guess is too low.${end}"
    printf "Guess again: " ; declare -i guess ; read -r guess
    if [[ $guess -eq $x ]] ; then
      printf "%s\n" "${blue}Congratulations! $guess is correct!${end}"
    fi
  fi
done
