import json
import random

# Load the JSON file
def load_champions():
    with open('champions.json', 'r') as f:
        champions = json.load(f)
    return champions

# Choose a random champion
def choose_random_champion(champions):
    return random.choice(champions)

# Get user feedback on the champion
def get_user_feedback(champion):
    is_correct = input(f"Is the champion {champion['Champion']}? (yes/no): ")
    if is_correct.lower() == 'yes':
        return True
    feedback = {}
    for field in champion:
        if field == "Champion":
            continue
        value = ', '.join(champion[field]) if isinstance(champion[field], list) else champion[field]
        if field == "Release year":
            feedback[field] = input(f"Is the {field} ({value}) correct for {champion['Champion']}? (yes/higher/lower): ")
        else:
            feedback[field] = input(f"Is the {field} ({value}) correct for {champion['Champion']}? (yes/no/partial): ")
    return feedback

# Filter champions based on user feedback
def filter_champions(champions, feedback, guessed_champion):
    for field in feedback:
        if feedback[field] == 'yes':
            champions = [champion for champion in champions if champion[field] == guessed_champion[field]]
        elif feedback[field] == 'no':
            champions = [champion for champion in champions if champion[field] != guessed_champion[field]]
        elif feedback[field] == 'higher':
            champions = [champion for champion in champions if champion[field] > guessed_champion[field]]
        elif feedback[field] == 'lower':
            champions = [champion for champion in champions if champion[field] < guessed_champion[field]]
        elif feedback[field] == 'partial':
            champions = [champion for champion in champions if guessed_champion[field] in champion[field]]
    return champions

# Initialize scores
def initialize_scores(champions):
    return {champion['Champion']: 0 for champion in champions}

# Update scores based on user feedback
def update_scores(scores, champions, feedback, guessed_champion):
    for field in feedback:
        if feedback[field] == 'yes':
            for champion in champions:
                if champion[field] == guessed_champion[field]:
                    scores[champion['Champion']] += 1
        elif feedback[field] == 'no':
            for champion in champions:
                if champion[field] == guessed_champion[field]:
                    scores[champion['Champion']] -= 1
        elif feedback[field] == 'higher':
            for champion in champions:
                if champion[field] > guessed_champion[field]:
                    scores[champion['Champion']] += 1
        elif feedback[field] == 'lower':
            for champion in champions:
                if champion[field] < guessed_champion[field]:
                    scores[champion['Champion']] += 1
        elif feedback[field] == 'partial':
            for champion in champions:
                if guessed_champion[field] in champion[field]:
                    scores[champion['Champion']] += 0.5
    return scores

# Choose the most probable champion
def choose_most_probable_champion(champions, scores):
    max_score = max(scores.values())
    most_probable_champions = [champion for champion in champions if scores[champion['Champion']] == max_score]
    return random.choice(most_probable_champions)

# Main function
def main():
    champions = load_champions()
    scores = initialize_scores(champions)
    while len(champions) > 1:
        guessed_champion = choose_most_probable_champion(champions, scores)
        feedback = get_user_feedback(guessed_champion)
        if feedback is True:
            print(f"The champion is: {guessed_champion['Champion']}")
            return
        scores = update_scores(scores, champions, feedback, guessed_champion)
        champions = filter_champions(champions, feedback, guessed_champion)
    if champions:
        print(f"The champion is: {champions[0]['Champion']}")
    else:
        print("No matching champion found.")

if __name__ == "__main__":
    main()