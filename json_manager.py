import os
import json


# This program is a JSON manager that can read and write JSON files.
# The format of the JSON file is as follows:
# {
#     "Champion": "value1",
#     "Gender": "value2",
#     "Position(s)": "value3",
#     "Species": "value4",
#     "Resource": "value5"
#     "Range type": "value6"
#     "Region(s)": "value7"
#     "Release year": "value8"
# }

Genders = ["Male", "Female", "Other"]
Positions = ["Top", "Jungle", "Middle", "Bottom", "Support"]
Species = ["Human", "Yordle", "Vastayan", "Magicborn", 
           "Darkin", "Minotaur", "Undead", "God", 
           "Spirit", "Spiritualist", "Iceborn", 
           "Celestial", "Dragon", "God-Warrior" ,"Void-Being",
           "Golem", "Magically Altered", "Cyborg"]
Resources = ["Mana", "Energy", "Manaless", "Health costs"]
RangeTypes = ["Melee", "Ranged"]
Regions = ["Demacia", "Noxus", "Ionia", "Zaun", 
           "Freljord", "Targon", "Bilgewater", 
           "Shadow Isles", "Shurima", "Ixtal", 
           "Runeterra", "Bandle City", "Void",
           "Piltover"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_actual_champions(Champion_name):
    clear_screen()
    print("Champion: ", Champion_name)
    print("")


# Function to read JSON file
def read_json_file(file_name):
    if os.path.exists(file_name) and os.path.getsize(file_name) > 0:
        with open(file_name, "r") as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError:
                print(f"Error: {file_name} is not a valchampion JSON file.")
                return []
    else:
        print(f"Error: {file_name} does not exist or is empty.")
        return []

# Function to write JSON file
def write_json_file(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

# Function to add a new entry to the JSON file
def add_entry(file_name, new_entry):
    data = read_json_file(file_name)
    data.append(new_entry)
    write_json_file(file_name, data)

# Function to delete an entry from the JSON file
def delete_entry(file_name, entry_Champion):
    data = read_json_file(file_name)
    for entry in data:
        if entry["Champion"] == entry_Champion:
            data.remove(entry)
            write_json_file(file_name, data)
            return
    print("Entry not found!")

# Function to update an entry in the JSON file
def update_entry(file_name, entry_champion, updated_entry):
    data = read_json_file(file_name)
    for i, entry in enumerate(data):
        if entry["champion"] == entry_champion:
            data[i] = updated_entry
            write_json_file(file_name, data)
            return
    print("Entry not found!")

# Function that let the user enter all the data for a new entry
def get_user_input(prompt, options, multiple=False):
    while True:
        print(prompt)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        user_input = input("Choose an option (use comma to separate multiple options): ").split(',')
        if all(choice.isdigit() and 1 <= int(choice) <= len(options) for choice in user_input):
            if multiple:
                return [options[int(choice) - 1] for choice in user_input]
            else:
                return options[int(user_input[0]) - 1]
        else:
            print("Invalid input. Please choose a valid option.")

def enter_new_entry():
    new_entry = {}
    clear_screen()
    new_entry["Champion"] = input("Enter Champion: ")
    display_actual_champions(new_entry["Champion"])
    new_entry["Gender"] = get_user_input("Enter Gender", Genders)
    display_actual_champions(new_entry["Champion"])
    new_entry["Position(s)"] = get_user_input("Enter Position(s)", Positions, multiple=True)
    display_actual_champions(new_entry["Champion"])
    new_entry["Species"] = get_user_input("Enter Species", Species, multiple=True)
    display_actual_champions(new_entry["Champion"])
    new_entry["Resource"] = get_user_input("Enter Resource", Resources)
    display_actual_champions(new_entry["Champion"])
    new_entry["Range type"] = get_user_input("Enter Range type", RangeTypes)
    display_actual_champions(new_entry["Champion"])
    new_entry["Region(s)"] = get_user_input("Enter Region(s)", Regions, multiple=True)
    display_actual_champions(new_entry["Champion"])
    new_entry["Release year"] = input("Enter Release year: ")
    return new_entry

# Main function to manage the JSON file
def main():
    file_name = "champions.json"
    while True:
        # print("1. Read JSON file")
        # print("2. Write JSON file")
        # print("3. Add entry")
        # print("4. Delete entry")
        # print("5. Update entry")
        # print("6. Exit")
        # choice = int(input("Enter your choice: "))
        choice = 3
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
        else:
            print("Invalchampion choice!")

if __name__ == "__main__":
    main()