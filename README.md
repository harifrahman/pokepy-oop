# Pokemon Battle Simulator (pokepy-oop)

Arif learn OOP implementation in python

This repository is a simple project to learn Object-Oriented Programming (OOP) in Python by simulating a battle between two Pokemon.

## Overview

In this project, we will create a Pokemon battle simulator where each Pokemon has health points (HP) and attack points (AP). Two Pokemon will battle each other, and the one with the higher remaining health points after the battle will be declared the winner.

## Features

- Define a `Pokemon` class with attributes for name, health points, and attack points.
- Implement methods for attacking another Pokemon and reducing health points.
- Simulate a battle between two Pokemon and determine the winner.

## Classes

### Pokemon

The `Pokemon` class will have the following attributes and methods:

- **Attributes:**
  - `name`: The name of the Pokemon.
  - `health_points`: The health points of the Pokemon.
  - `attack_points`: The attack points of the Pokemon.

- **Methods:**
  - `attack(pokemon)`: Attacks another Pokemon and reduces their health points.
  - `is_defeated()`: Checks if the Pokemon's health points are zero or less.

## Example Usage

Here is an example of how to use the `Pokemon` class to simulate a battle from console:


1. navigate to root project directory
2. execute 

```sh
  python app.py
```
3. setup Pokemon A and Pokemon B information
4. After that, log will be printed info about iteration fight-stage
5. Getting winner


## Getting Started

1. Clone the repository:
    ```sh
    git clone git@github.com:harifrahman/pokepy-oop.git 
    cd pokepy-oop
    ```

2. Run the example script:
    ```sh
    python3 app.py
    ```

## Contributing

Feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License.