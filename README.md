# Rock, Paper, Scissors Game

A simple Rock, Paper, and Scissors game implemented in Python. This project is part of my programming journey, showcasing my learning progress and understanding of basic Python concepts.

## How to Play

1. Clone the repository to your local machine.
2. Run the Python script.
3. Enter your choice: `r` for Rock, `p` for Paper, or `s` for Scissors.
4. The computer will randomly choose its move.
5. The result will be displayed: Win, Lose, or Draw.

## Code Explanation

### Assumptions

- Rock is represented by `1`
- Paper is represented by `0`
- Scissors is represented by `-1`

### Game Logic

The game uses a simple function to determine the result:

```python
def result(user, computer):
    if(user == computer):
        print("Draw!")
    elif(user-computer == 1 or user-computer == -2):
        print("You lose!")
    else:
        print("You won!")
```

### How it works

- The computer makes a random choice between Rock, Paper, and Scissors.
- The user inputs their choice.
- The program maps the user input to the corresponding value and calculates the result.
- The result is displayed along with the choices made by both the user and the computer.

## Sample Code

Here's the complete code for the game:

```python
import random

# Assumptions:
# Rock -> 1
# Paper -> 0
# Scissors -> -1

def result(user, computer):
    if(user == computer):
        print("Draw!")
    elif(user-computer == 1 or user-computer == -2):
        print("You lose!")
    else:
        print("You won!")

computer = random.randint(-1,1)

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
    print(f"You chose: {user}\nComputer chose: {reverse_mapping[computer]}")
else:
    print("Invalid Input!")
```

## Future Enhancements

- Add a graphical user interface (GUI) for a more interactive experience.
- Implement a score tracker to keep track of wins, losses, and draws.
- Expand the game to include more complex rules or variations.

## Contributing

If you have suggestions or improvements, feel free to open an issue or submit a pull request. Contributions are always welcome!

## License

This project is open-source and available under the MIT License.

---

Follow my [GitHub](https://github.com/sahilahmad6569) to stay updated with my programming journey and other projects.
