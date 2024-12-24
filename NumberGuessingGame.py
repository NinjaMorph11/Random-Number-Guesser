import random
print("Hello. What is your name?")
name = input()
secretNumber = random.randit(1, 20)
print("Well, " + name +
      ", I am thinking of a number between 1 to 20, guess which number.")

# Asking the player to guess 6 times

for guesstaken in range(1, 7):
    print("Take a guess")
    guess = int(input())
    if guess < secretNumber:
        print("Your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break  # This condition is the correct guess

if guess == secretNumber:
    print("Nice! You guessed the correct number!")
else:
    print("Nope, I was thinking of a different number")
