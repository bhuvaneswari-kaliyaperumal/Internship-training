target=50
guess=int(input("Enter Guess number:"))
target = 50
guess = int(input("Enter Guess number: "))
while guess != target:
    if(guess<  target):
        print("The number is lesser than Target numer, please enter Higher Number")
    else:
        print("The number is Higher than Target numer, please enter Lesser Number")
    guess=int(input("enter number again:"))
else:
    print("Congratulations! You guessed the correct number.")

"""Enter Guess number:30
Enter Guess number: 35
The number is lesser than Target numer, please enter Higher Number
enter number again:45
The number is lesser than Target numer, please enter Higher Number
enter number again:48
The number is lesser than Target numer, please enter Higher Number
enter number again:50
Congratulations! You guessed the correct number."""