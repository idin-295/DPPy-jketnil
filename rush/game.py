import os
import time
player_inventory = set()
joseph_room = {
    "description": (
        "You enter Joseph Joestar's bedroom. "
        "The room is messy and filled with old furniture."
    ),

    "objects": {
        1: {
            "name": "Bed",
            "description": "The blanket is messy. Someone slept here recently."
        },
        2: {
            "name": "Wardrobe",
            "description": "You find old coats and a photograph."
        },
        3: {
            "name": "Desk",
            "description": "There is an old map and a mysterious note."
        },
        4: {
            "name": "Leather suitcase",
            "description": "The suitcase is locked. Something rattles inside."
        },
        5: {
            "name": "Pocket watch",
            "description": "The watch has stopped at 3:15."
        }
    }
}

npcs = {
    "old_man": {
        "name": "Old Man",
        "role": "Dorm Owner",
        "room": 0,
        "dialogue": (
            "Oh! Hello there, young man. Are you the new tenant?\n"
            "Could you do an old man a favor?\n"
            "I've forgotten where I put something important.\n"
            "It's a small brass key. I think I left it somewhere "
            "in this dorm.\n"
            "Could you look around and find it for me?\n"
            "Oh, and if you find my notebook, bring that back too!\n"
            "Now... what was I looking for again?"
        ),
        "quest": {
            "name": "The Missing Brass Key",
            "target_item": "brass_key",
            "optional_item": "old_notebook",
            "completed": False
        }
    }
}

choice = 0

print( "==",npcs["old_man"]["name"], "==")
print(npcs["old_man"]["dialogue"])
time.sleep(7)


def main():
    while True :
        os.system("cls" if os.name == "nt" else "clear")
        print("========= MAIN =========")
        print("1.room1")
        print("2.room2")
        print("3.room3")
        print("4.room4")
        print("5. EXIT")
        choice = int(input("chose 1-5 :"))
        match choice :
            case 1:
                room_of_john() 
            case 2:
                room_of_jorh()
            case 3 :
                room_of_joseph()
            case 4 :
                room_of_jostar()
            case 5 :
                room_of_jojo()
def room_of_john():
        while True :
            os.system("cls" if os.name == "nt" else "clear")        
            print("you go to room number 1 and enter the room.")
            print("1. wardrome")
            print("2. table,chair")
            print("3. storage box")
            print("4. bed")
            print("5. EXIT",)
            choice = int(input("chose 1-5 :"))
            match choice:
                    case 1:
                        print("in wardrome not have anything it's emty ")
                        time.sleep(5)
                    case 2 :
                        print("on table doesn't have anything and on chair too")
                        time.sleep(3)
                    case 3 :
                        print("you walk to be do you want to sleep for save ")
                    case 4 :
                        print("you walk to storage box you open it,It have spyder web and some dusk")
                        time.sleep(3)
                    case 5 :
                        print("exit to main hall")
                        time.sleep(3)
                        break
def room_of_jorh() :
        print("2. you go to room number 2 and enter the room")
        while True :
            os.system("cls" if os.name == "nt" else "clear")        
            print("you go to room number 1 and enter the room.")
            print("1. beoken wardrome")
            print("2. rusty table leg with damp wood tabletop and a chair that missing 1 leg")
            print("3. storage box with broken box lid")
            print("4. bed with a torn be sheet")
            print("5.EXIT",)
            choice = int(input("chose 1-5 :"))
            match choice:
                    case 1:
                        print("in wardrome is broken anything it's emty ")
                        time.sleep(5)
                    case 2 :
                        print("on table doesn't have anything and on chair too")
                        time.sleep(3)
                    case 3 :
                        print("you walk to be do you want to sleep for save ")
                    case 4 :
                        print("you walk to storage box you open it,It have spyder web and some dusk")
                        time.sleep(3)
                    case 5 :
                        print("exit to main hall")
                        time.sleep(3)
                        break         

def room_of_joseph():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("\n====== JOSEPH'S ROOM ======")
        print(joseph_room["description"])

        print("\n1. Bed")
        print("2. Wardrobe")
        print("3. Desk")
        print("4. Leather suitcase")
        print("5. Pocket watch")
        print("6. Return to main hall")

        try:
            choice = int(input("Choose 1-6: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if choice in joseph_room["objects"]:
            obj = joseph_room["objects"][choice]
            print(f"\nYou inspect the {obj['name']}.")
            print(obj["description"])
            input("\nPress Enter to continue...")

        elif choice == 6:
            print("You leave Joseph's room.")
            break

        else:
            print("Invalid choice.")


def room_of_jostar() :
        print("4. you go to room number 4")
        while True :
            os.system("cls" if os.name == "nt" else "clear")        
            print("you go to room number 1 and enter the room.")
            print("1. model airplanes on the table")
            print("2. you saw a old brown fedora hat hang")
            print("4. storage box")
            print("5. bed")
            print("5. EXIT",)
            choice = int(input("chose 1-5 :"))
            match choice:
                    case 1:
                        print("in wardrome not have anything it's emty ")
                        time.sleep(5)
                    case 2 :
                        print("on table doesn't have anything and on chair too")
                        time.sleep(3)
                    case 3 :
                        print("you walk to be do you want to sleep for save ")
                    case 4 :
                        print("you walk to storage box you open it,It have spyder web and some dusk")
                        time.sleep(3)
                    case 5 :
                        print("exit to main hall")
                        time.sleep(3)
                        break

def room_of_jojo() :
            print("you go to EXIT door and go out off building,GOODBYE")
            exit()


main()