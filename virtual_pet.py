
print("================================")
print("       VIRTUAL PET SIMULATOR")
print("================================")

# Store pet information
pet = {
    "name": "",
    "hunger": 50,
    "happiness": 50,
    "energy": 50
}

# Store actions
actions = ["Feed", "Play", "Sleep", "Check Status", "Exit"]

# Get pet name
pet["name"] = input("Enter your pet's name: ")

print("\nYou adopted", pet["name"], "!")
print("Take good care of your pet!")

# Feed function
def feed_pet():
    print("\nYou are feeding", pet["name"])

    pet["hunger"] -= 20

    if pet["hunger"] < 0:
        pet["hunger"] = 0

    pet["happiness"] += 5

    if pet["happiness"] > 100:
        pet["happiness"] = 100

    print(pet["name"], "has eaten!")
    print("Hunger:", pet["hunger"])

# Play function
def play_pet():
    if pet["energy"] < 15:
        print("\nYour pet is too tired to play!")
        print("Let it sleep first.")
    else:
        pet["happiness"] += 20
        pet["energy"] -= 15
        pet["hunger"] += 10

        if pet["happiness"] > 100:
            pet["happiness"] = 100

        if pet["hunger"] > 100:
            pet["hunger"] = 100

        print("\nYou played with", pet["name"], "!")
        print("Your pet is happy!")

# Sleep function
def sleep_pet():
    pet["energy"] += 30

    if pet["energy"] > 100:
        pet["energy"] = 100

    print("\n", pet["name"], "is sleeping...")
    print("Energy:", pet["energy"])

# Status function
def check_status():
    print("\n========== PET STATUS ==========")
    print("Name:", pet["name"])
    print("Hunger:", pet["hunger"], "/100")
    print("Happiness:", pet["happiness"], "/100")
    print("Energy:", pet["energy"], "/100")

    if pet["hunger"] >= 80:
        print("Your pet is very hungry!")

    if pet["happiness"] < 30:
        print("Your pet is feeling sad!")

    if pet["energy"] < 20:
        print("Your pet is very tired!")

    print("================================")

# Main game loop
while True:
    print("\n========== MENU ==========")

    for i in range(len(actions)):
        print(i + 1, ".", actions[i])

    choice = input("\nChoose an action (1-5): ")

    if choice == "1":
        feed_pet()

    elif choice == "2":
        play_pet()

    elif choice == "3":
        sleep_pet()

    elif choice == "4":
        check_status()

    elif choice == "5":
        print("\nGoodbye!")
        print("Take care of", pet["name"], "!")
        break

    else:
        print("\nInvalid choice! Please choose 1-5.")
