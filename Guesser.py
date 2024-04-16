import json
import random
import os

# list of all the possible values for each field
# These are used to initialize the probabilities
Genders = ["Male", "Female", "Other"]
Positions = ["Top", "Jungle", "Middle", "Bottom", "Support"]
Species = ["Human", "Yordle", "Vastayan", "Magicborn", 
           "Darkin", "Minotaur", "Undead", "God", 
           "Spirit", "Spiritualist", "Iceborn", 
           "Celestial", "Dragon", "God-Warrior" ,"Void-Being",
           "Golem", "Magically Altered", "Cyborg",
           "Aspect", "Chemically Altered", "Demon",
           "Unknown", "Troll", "Rat", "Cat", "Revenant",
           "Dragon", "Brackern", "Yeti", "Dog"]
Resources = ["Mana", "Energy", "Manaless", "Health costs",
            "Rage", "Courage", "Ferocity", "Heat", "Fury",
            "Flow", "Grit", "Shield", "Bloodthirst"]
RangeTypes = ["Melee", "Ranged"]
Regions = ["Demacia", "Noxus", "Ionia", "Zaun", 
           "Freljord", "Targon", "Bilgewater", 
           "Shadow Isles", "Shurima", "Ixtal", 
           "Runeterra", "Bandle City", "Void",
           "Piltover", "Camavor", "Icathia",]

def create_specific_folder(folder_name):
    """
    Create a specific folder in the user's AppData Local directory.

    Args:
        folder_name (str): The name of the folder to create.
    """
    # Define the path of the new folder
    new_folder_path = os.path.join(os.getenv('LOCALAPPDATA'), folder_name)

    # Create the new folder if it doesn't already exist
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

# Load the JSON file
def load_champions():
    """
    Load the champions data from a JSON file in the AppData Local directory.

    Returns:
        list: A list of dictionaries, where each dictionary contains the data for one champion.
    """
    # Define the path of the JSON file
    json_file_path = os.path.join(os.getenv('LOCALAPPDATA'), 'Loldle_Solver', 'champions.json')

    with open(json_file_path, 'r') as f:
        champions = json.load(f)
    return champions

# Choose a random champion
def choose_random_champion(champions):
    return random.choice(champions)

# Get user feedback on the champion
def get_user_feedback(champion):
    feedback = {}
    for field in champion:
        if field == "Champion":
            is_correct = input(f"Is the champion {champion['Champion']}? (y for yes/n for no): ")
            if is_correct.lower() == 'y':
                return True
            else:
                feedback[field] = 'n'
        else:
            value = ', '.join(champion[field]) if isinstance(champion[field], list) else champion[field]
            if field == "Release year":
                feedback[field] = input(f"Is the {field} ({value}) correct for {champion['Champion']}? (y for yes/h for higher/l for lower): ")
            else:
                feedback[field] = input(f"Is the {field} ({value}) correct for {champion['Champion']}? (y for yes/n for no/p for partial): ")
    return feedback

# Filter champions based on user feedback
def filter_champions(champions, feedback, guessed_champion):
    """
    Filter the list of champions based on the user's feedback.

    Args:
        champions (list): The current list of possible champions.
        feedback (dict): The user's feedback on the guessed champion.
        guessed_champion (dict): The champion that was guessed.

    Returns:
        list: The filtered list of champions.
    """
    for field in feedback:
        if feedback[field] == 'y':
            champions = [champion for champion in champions if champion[field] == guessed_champion[field]]
        elif feedback[field] == 'n':
            champions = [champion for champion in champions if champion[field] != guessed_champion[field]]
        elif feedback[field] == 'h':
            champions = [champion for champion in champions if champion[field] > guessed_champion[field]]
        elif feedback[field] == 'l':
            champions = [champion for champion in champions if champion[field] < guessed_champion[field]]
        elif feedback[field] == 'p':
            champions = [champion for champion in champions if set(guessed_champion[field]).intersection(champion[field])]
    return champions

# Initialize probabilities
def initialize_probabilities(champions, fields):
    probabilities = {field: {value: 0 for value in fields[field]} for field in fields}
    for champion in champions:
        for field in champion:
            if field in probabilities:
                if isinstance(champion[field], list):
                    for value in champion[field]:
                        probabilities[field][value] += 1
                else:
                    probabilities[field][champion[field]] += 1
    for field in probabilities:
        total = sum(probabilities[field].values())
        if total != 0:
            for value in probabilities[field]:
                probabilities[field][value] /= total
    return probabilities

# Update probabilities based on user feedback
def update_probabilities(probabilities, champions, feedback):
    for field in feedback:
        if field in probabilities:
            if feedback[field] in ['n', 'h', 'l']:
                for value in probabilities[field]:
                    probabilities[field][value] = 0
            elif feedback[field] == 'p':
                for value in probabilities[field]:
                    if value not in champions[0][field]:
                        probabilities[field][value] = 0
            total = sum(probabilities[field].values())
            if total != 0:
                for value in probabilities[field]:
                    probabilities[field][value] /= total
    return probabilities

# Choose the most probable champion
def choose_most_probable_champion(champions, probabilities):
    scores = {champion['Champion']: 0 for champion in champions}
    for champion in champions:
        for field in champion:
            if field in probabilities:
                if isinstance(champion[field], list):
                    for value in champion[field]:
                        scores[champion['Champion']] += probabilities[field][value]
                else:
                    scores[champion['Champion']] += probabilities[field][champion[field]]
    max_score = max(scores.values())
    most_probable_champions = [champion for champion in champions if scores[champion['Champion']] == max_score]
    return random.choice(most_probable_champions)

# Main function
def main():
    """
    The main function of the program. It loads the champions data, initializes the probabilities,
    and then enters a loop where it guesses a champion, gets the user's feedback, filters the
    champions based on the feedback, and updates the probabilities. The loop continues until
    there is only one champion left or the user confirms the guessed champion.
    """
    create_specific_folder("Loldle_Solver")
    champions = load_champions()
    fields = {"Gender": Genders, "Position": Positions, "Species": Species, "Resource": Resources, "Range type": RangeTypes, "Region": Regions}
    probabilities = initialize_probabilities(champions, fields)
    while len(champions) > 1:
        guessed_champion = choose_most_probable_champion(champions, probabilities)
        feedback = get_user_feedback(guessed_champion)
        if feedback is True:
            print(f"The champion is: {guessed_champion['Champion']}")
            return
        champions = filter_champions(champions, feedback, guessed_champion)
        probabilities = update_probabilities(probabilities, champions, feedback)
    if champions:
        print(f"The champion is: {champions[0]['Champion']}")
    else:
        print("No matching champion found.")

if __name__ == "__main__":
    main()