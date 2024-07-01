import random

# Assumptions:
# Rock -> 1
# Paper -> 0
# Scissors -> -1

def result(user, computer):
    if(user == computer):
        print("Draw!")

    # elif(user == 1 and computer == -1): 2 
    #     print("You won!")
    # elif(user == -1 and computer == 1): -2
    #     print("You lose!")
    # elif(user == 1 and computer == 0): 1
    #     print("You lose!")
    # elif(user == 0 and computer == 1): -1
    #     print("You won!")
    # elif(user == -1 and computer == 0): -1
    #     print("You won!")
    # elif(user == 0 and computer == -1): 1
    #     print("You lose!")

# **********Better Approach (Less readability)**********
    elif(user-computer == 1 or user-computer == -2):
        print("Your lose!")
    else:
        print("Your won!")

computer = random.randint(-1,1)
# print(computer)

valid_inputs = ["r", "p", "s"]

mapping = {
    "r":1,
    "p":0,
    "s":-1
}

reverse_mapping = {
    1:"r",
    0:"p",
    -1:"s",
}
user = input("Enter 'r' for Rock, 'p' for Paper, or 's' for Scissors: ")

if(user in valid_inputs):
    result(mapping[user], computer)
    print(f"You choosed: {user}\nComputer choosed: {reverse_mapping[computer]}")
else:
    print("Invalid Input!")