
#To guess the correct birthdate and return the number of guesses it takes.
birthdate = 5
attempts = 0

while True:
  attempts += 1

  guess = int(input("Guess the number: \n"))
  if guess>birthdate:
    print("Your guess is High")

  elif guess<birthdate:
    print("Your guess is Low")

  else:
    print(f"You guessed the correct date in {attempts} attempts")
    break

print("Congrats,You won the guess!")