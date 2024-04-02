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

- `Champion_Guesser.py`: This is the main script for the guessing game. It uses the data loaded by `json_manager.py` to guess a champion based on user feedback.

### How to Run

1. Ensure you have Python installed on your machine.

2. Run the `Champion_Guesser.py` script:

```bash
python Champion_Guesser.py
```

3. The program will guess a champion and ask for your feedback. You can respond with 'yes', 'no', 'higher', 'lower', or 'partial' for each field.

4. The program will continue guessing until it correctly identifies the champion.

## Future Work

This project is a work in progress. Future components will add more functionality and depth to the Loldle Solver.