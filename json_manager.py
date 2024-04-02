# Importing necessary libraries
import os
import json

# Defining constants
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

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to display the current champion
def display_actual_champions(Champion_name):
    clear_screen()
    print("Champion: ", Champion_name)
    print("")

# Function to read JSON file
def read_json_file(file_name):
    # Check if file exists and is not empty
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, "r") as file:
            try:
                # Load JSON data from file
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                # Handle JSON decoding errors
                print(f"Error: {file_name} is not a valid JSON file.")
                return []
    else:
        # Handle file not found or empty file errors
        print(f"Error: {file_name} does not exist or is empty.")
        return []

# Function to write JSON file
def write_json_file(file_name, data):
    with open(file_name, "w") as file:
        # Dump JSON data to file
        json.dump(data, file, indent=4)

# Function to add a new entry to the JSON file
def add_entry(file_name, new_entry):
    # Read existing data
    data = read_json_file(file_name)
    # Append new entry
    data.append(new_entry)
    # Write back to file
    write_json_file(file_name, data)

# Function to delete an entry from the JSON file
def delete_entry(file_name, entry_Champion):
    # Read existing data
    data = read_json_file(file_name)
    for entry in data:
        # Find and remove the entry
        if entry["Champion"] == entry_Champion:
            data.remove(entry)
            # Write back to file
            write_json_file(file_name, data)
            return
    print("Champion not found!")

# Function to update an entry in the JSON file
def update_entry(file_name, entry_champion, updated_entry):
    # Read existing data
    data = read_json_file(file_name)
    for i, entry in enumerate(data):
        # Find and update the entry
        if entry["champion"] == entry_champion:
            data[i] = updated_entry
            # Write back to file
            write_json_file(file_name, data)
            return
    print("Champion not found!")

# Function that let the user enter all the data for a new entry
def get_user_input(prompt, options, multiple=False):
    while True:
        print(prompt)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        user_input = input("Choose an option (use comma to separate multiple options): ").split(',')
        # Validate user input
        if all(choice.isdigit() and 1 <= int(choice) <= len(options) for choice in user_input):
            if multiple:
                return [options[int(choice) - 1] for choice in user_input]
            else:
                return options[int(user_input[0]) - 1]
        else:
            print("Invalid input. Please choose a valid option.")

# Function to check if a champion already exists
def champion_exists(champion_name):
    # Load the JSON file
    with open('champions.json', 'r') as f:
        champions = json.load(f)

    # Check if the champion is in the list
    for champion in champions:
        if champion["Champion"].lower() == champion_name.lower():
            return True

    return False

# Function to enter a new entry
def enter_new_entry():
    new_entry = {}
    clear_screen()
    while True:
        champion_name = input("Enter Champion: ")
        if not champion_exists(champion_name):
            new_entry["Champion"] = champion_name
            break
        else:
            print("This champion already exists. Please enter a different champion.")
    display_actual_champions(new_entry["Champion"])

    entry_fields = [
        {"name": "Gender", "options": Genders, "multiple": False},
        {"name": "Position(s)", "options": Positions, "multiple": True},
        {"name": "Species", "options": Species, "multiple": True},
        {"name": "Resource", "options": Resources, "multiple": False},
        {"name": "Range type", "options": RangeTypes, "multiple": False},
        {"name": "Region(s)", "options": Regions, "multiple": True},
    ]

    for field in entry_fields:
        new_entry[field["name"]] = get_user_input(f"Enter {field['name']}", field["options"], field["multiple"])
        display_actual_champions(new_entry["Champion"])

    new_entry["Release year"] = input("Enter Release year: ")
    return new_entry

def get_choice(prompt, num_choices):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= num_choices:
                return choice
            else:
                print("Invalid choice!")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    file_name = "champions.json"
    while True:
        print("1. Read JSON file")
        print("2. Write JSON file")
        print("3. Add entry")
        print("4. Delete entry")
        print("5. Update entry")
        print("6. Exit")
        choice = get_choice("Enter your choice: ", 6)
        if choice == 1:
            data = read_json_file(file_name)
            for entry in data:
                print(entry)
        elif choice == 2:
            data = read_json_file(file_name)
            write_json_file(file_name, data)
        elif choice == 3:
            new_entry = enter_new_entry()
            add_entry(file_name, new_entry)
        elif choice == 4:
            entry_champion = input("Enter champion of entry to delete: ")
            delete_entry(file_name, entry_champion)
        elif choice == 5:
            entry_champion = input("Enter champion of entry to update: ")
            updated_entry = enter_new_entry()
            update_entry(file_name, entry_champion, updated_entry)
        elif choice == 6:
            break

# Entry point of the script
if __name__ == "__main__":
    main()