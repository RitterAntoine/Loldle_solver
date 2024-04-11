# Loldle Solver

Loldle Solver is a project inspired by the web game LoLdle, developed by Reddit user Pimeko for fans of League of Legends. LoLdle, is a game where players guess a League of Legends champion each day, with everyone having the same champion to guess.

The Loldle Solver project aims to create a comprehensive solution for solving and understanding various aspects of the game League of Legends. It includes components like the Champion Guesser, which is a guessing game where the program tries to guess a League of Legends champion based on user feedback.

The Champion Guesser, similar to LoLdle, provides hints about the champion's properties like gender, positions, species, etc., to help players get closer to the answer. All the data used in this project is provided by League of Legends Fandom.

This project is a work in progress, with future components planned to add more functionality and depth to the Loldle Solver.

## Champion Guesser

The Champion Guesser is a guessing game where the program tries to guess a League of Legends champion based on user feedback.

### Files

- `champions.json`: This file contains data about the champions in League of Legends. Each champion is represented as a JSON object with fields for the champion's name, release year, and other attributes.

- `json_manager.py`: This script contains functions for loading the champions data from the `champions.json` file.

- `Guesser.py`: This is the main script for the guessing game. It uses the data loaded by `json_manager.py` to guess a champion based on user feedback.

### How to Run

1. Ensure you have Python installed on your machine.

2. Run the `Guesser.py` script:

```bash
python Guesser.py
```

3. The program will guess a champion and ask for your feedback. You can respond with 'y' for 'yes', 'n' for 'no', 'h' for 'higher', 'l' for 'lower', or 'p' for 'partial' for each field.

4. The program will continue guessing until it correctly identifies the champion.

## Algorithm Tester

The `Algorithm_tester.py` script is used to test the effectiveness of the Champion Guesser. It runs the guessing algorithm on each champion multiple times and calculates the average number of guesses needed to correctly identify each champion.

### How to Run

1. Ensure you have Python installed on your machine.

2. Run the `Algorithm_tester.py` script:

```bash
python Algorithm_tester.py
```

3. The script will run the guessing algorithm on each champion 100 times (this number can be adjusted in the script) and print out the average number of guesses needed for each champion.

4. At the end, the script will print out the overall average number of guesses needed to guess all champions, as well as the total time taken to run the tests.

### Understanding the Output

The output of the Algorithm_tester.py script is structured as follows:

- For each champion, the script prints the champion's name followed by the average number of guesses needed to guess that champion over the number of tests run.

- After testing all champions, the script prints the overall average number of guesses needed to guess all champions.

- Finally, the script prints the total time taken to run all the tests.

This output can be used to evaluate the effectiveness of the guessing algorithm and identify areas for improvement.

## Future Work

This project is a work in progress. Future components will add more functionality and depth to the Loldle Solver.
