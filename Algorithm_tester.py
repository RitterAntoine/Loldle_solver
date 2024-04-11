import time
from Guesser import load_champions, initialize_probabilities, choose_most_probable_champion, filter_champions, update_probabilities, Genders, Positions, Species, Resources, RangeTypes, Regions

def test_algorithm(champion_to_guess):
    champions = load_champions()
    fields = {"Gender": Genders, "Position": Positions, "Species": Species, "Resource": Resources, "Range type": RangeTypes, "Region": Regions}
    probabilities = initialize_probabilities(champions, fields)
    guesses = 0
    while len(champions) > 1:
        guessed_champion = choose_most_probable_champion(champions, probabilities)
        guesses += 1
        if guessed_champion['Champion'] == champion_to_guess['Champion']:
            return guesses
        feedback = {field: 'y' if guessed_champion[field] == champion_to_guess[field] else 'n' for field in guessed_champion}
        champions = filter_champions(champions, feedback, guessed_champion)
        probabilities = update_probabilities(probabilities, champions, feedback)
    return guesses

def test_all_champions():
    champions = load_champions()
    results = {}
    total_guesses = 0
    tests_per_champion = 100
    for champion in champions:
        for _ in range(tests_per_champion):
            guesses = test_algorithm(champion)
            total_guesses += guesses
        average_guesses_for_champion = total_guesses / tests_per_champion
        results[champion['Champion']] = average_guesses_for_champion
        total_guesses = 0
    print("\nChampion Guesses:")
    print("-----------------")
    for champion, average_guesses in results.items():
        print(f"{champion}: {average_guesses:.2f} average guesses over {tests_per_champion} tests")
    average_guesses = sum(results.values()) / len(champions)
    print("\nOverall Results:")
    print("----------------")
    print(f"Average guesses overall: {average_guesses:.2f}")

if __name__ == "__main__":
    start_time = time.time()
    test_all_champions()
    end_time = time.time()
    total_time = end_time - start_time
    print("\nTime Summary:")
    print("-------------")
    print(f"Total time: {total_time:.2f} seconds")