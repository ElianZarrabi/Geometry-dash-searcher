stats = {
    "Stereo Madness": ["Level 1", "Orbs: 50", "Dificulty: Easy"],
    "Back on Track": ["Level 2", "Orbs: 75", "Dificulty: Easy"],
    "Polargeist": ["Level 3", "Orbs: 100", "Dificulty: Normal"],
    "Dry Out": ["Level 4", "Orbs: 125", "Dificulty: Normal"],
    "Base After Base": ["Level 5", "Orbs: 150", "Dificulty: Hard"],
    "Can't Let Go": ["Level 6", "Orbs: 175", "Dificulty: Hard"],
    "Jumper": ["Level 7", "Orbs: 200", "Dificulty: Harder"],
    "Time Machine": ["Level 8", "Orbs: 225", "Dificulty: Harder"],
    "Cycles": ["Level 9", "Orbs: 250", "Dificulty: Harder"],
    "xStep": ["Level 10", "Orbs: 275", "Dificulty: Insane"],
    "Clutterfunk": ["Level 11", "Orbs: 300", "Dificulty: Insane"],
    "Theory of Everything": ["Level 12", "Orbs: 325", "Dificulty: Insane"],
    "Electroman Adventures": ["Level 13", "Orbs: 275", "Dificulty: Insane"],
    "Clubstep": ["Level 14", "Orbs: 500", "Dificulty: Demon"],
    "Electrodynamix": ["Level 15", "Orbs: 325", "Dificulty: Insane"],
    "Hexagon Force": ["Level 16", "Orbs: 325", "Dificulty: Insane"],
    "Blast Processing": ["Level 17", "Orbs: 275", "Dificulty: Harder"],
    "Theory of Everything 2": ["Level 18", "Orbs: 500", "Dificulty: Demon"],
    "Geometrical Dominator": ["Level 19", "Orbs: 275", "Dificulty: Harder"],
    "Deadlocked": ["Level 20", "Orbs: 500", "Dificulty: Demon"],
    "Fingerdash": ["Level 21", "Orbs: 325", "Dificulty: Insane"],
    "Dash": ["Level 22", "Orbs: 325", "Dificulty: Insane"],
}

def search_by_name():
    while True:    
        name = input("Enter the name of the level you want to search for: \n")
        stats_lower = {k.lower(): v for k, v in stats.items()}
        if name.lower() in stats_lower:
            return stats_lower[name.lower()]
        else:
            print("Level not found.")
            continue
def search_by_difficulty():
    while True:
        difficulty = input("Enter the difficulty of the level you want to search for: \n")
        results = {key: value for key, value in stats.items() if difficulty.lower() in value[2].lower()}
        if results:
            return results
        else:
            print("Difficulty not found.")

def search_by_orbs():
    while True:
        orbs = orbs_checker("Enter the number of orbs of the level you want to search for: \n")
        for key, value in stats.items():
            if str(orbs) == value[1].split(": ")[1]:
                return key, value
        else:
            print("Orbs not found.")
            continue
        

def orbs_checker(ask):
    while True:
        try:
            return int(input(ask))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

def search_by_level():
    while True:
        level = level_checker("Enter the level number of the level you want to search for: \n")
        for key, value in stats.items():
            if str(level) == value[0].split(" ")[1]:
                return key, value
                break
        else:
            print("Level not found.")
            continue

def level_checker(ask):
    while True:
        try:
            return int(input(ask))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

def main():
    print("------------ Geometry Dash Level Searcher ------------")
    while True:
        search_type = input("How do you want to search for the level? (name, difficulty, orbs, level, exit) \n")
        if search_type.lower() == "name":
            print(search_by_name())
            continue
        elif search_type.lower() == "difficulty":
            print(search_by_difficulty())
            continue
        elif search_type.lower() == "orbs":
            print(search_by_orbs())
            continue
        elif search_type.lower() == "level":
            print(search_by_level())
            continue
        elif search_type.lower() == "exit":
            break
        else:
            print("Invalid input. Please enter 'name', 'difficulty', 'orbs', 'level' or 'exit'.")
            continue

main()
input("Press Enter to exit...")