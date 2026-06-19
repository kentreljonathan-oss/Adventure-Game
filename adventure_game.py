import random

def show_welcome():
    print("=" * 50)
    print("WELCOME TO THE MYSTERIOUS FOREST ADVENTURE")
    print("=" * 50)
    print("You wake up at the edge of a dark forest.")
    print("Rumors say a hidden treasure lies within.")
    print("Your choices will decide your fate.")
    print("=" * 50)


def play_game():
    inventory = []
    score = 0

    show_welcome()
    print("\nYou are standing at a fork in the path.")
    print("1. Enter the dark forest")
    print("2. Walk along the river")
    print("3. Climb the rocky hill")

    choice = input("What do you choose? (1/2/3): ")

    if choice == "1":
        print("\nYou step into the forest. It is quiet, too quiet.")
        print("You find an old rusty sword on the ground.")
        inventory.append("rusty sword")
        score += 10
    elif choice == "2":
        print("\nYou walk along the river and find a shiny coin.")
        inventory.append("shiny coin")
        score += 5
    elif choice == "3":
        print("\nYou climb the hill and find a sturdy wooden shield.")
        inventory.append("wooden shield")
        score += 10
    else:
        print("\nYou hesitate and the path disappears.")
        print("A strange wind blows you back to the start.")
        score -= 5

    print(f"\nYour inventory: {inventory}")
    print(f"Current score: {score}")

    print("\nSuddenly, a wild goblin jumps out of the bushes!")
    print("1. Fight the goblin")
    print("2. Try to run away")
    print("3. Offer it an item from your inventory")

    battle_choice = input("What do you choose? (1/2/3): ")

    if battle_choice == "1":
        if "rusty sword" in inventory:
            print("\nYou swing your rusty sword and defeat the goblin!")
            score += 20
        else:
            print("\nYou fight with your bare hands and barely win.")
            score += 5
    elif battle_choice == "2":
        chance = random.randint(1, 2)
        if chance == 1:
            print("\nYou escape safely into a clearing.")
            score += 5
        else:
            print("\nThe goblin catches you and steals a coin!")
            if "shiny coin" in inventory:
                inventory.remove("shiny coin")
            score -= 10
    elif battle_choice == "3" and len(inventory) > 0:
        gift = inventory.pop()
        print(f"\nYou offer the {gift}. The goblin is pleased and leaves you alone.")
        score += 15
    else:
        print("\nYou have nothing to offer. The goblin scares you off.")
        score -= 5

    print(f"\nYour inventory: {inventory}")
    print(f"Current score: {score}")

    print("\nYou finally reach a glowing cave at the heart of the forest.")
    print("This could be where the treasure is hidden.")
    print("1. Enter the cave")
    print("2. Turn back home")

    final_choice = input("What do you choose? (1/2): ")

    if final_choice == "1":
        if score >= 30:
            print("\nYou enter confidently and find a chest of gold!")
            print("ENDING: TREASURE HUNTER VICTORY")
            score += 50
        else:
            print("\nYou enter but a trap collapses the cave behind you.")
            print("ENDING: TRAPPED IN THE DARK")
            score -= 10
    elif final_choice == "2":
        print("\nYou decide the forest is too dangerous and head home safely.")
        print("ENDING: SAFE BUT EMPTY HANDED")
    else:
        print("\nYou freeze in place and the sun sets. Night falls fast.")
        print("ENDING: LOST IN THE FOREST")
        score -= 5

    print(f"\nFinal inventory: {inventory}")
    print(f"Final score: {score}")
    print("=" * 50)


def main():
    playing = True
    while playing:
        play_game()
        again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if again == "yes":
            print("\nStarting a new adventure...\n")
        elif again == "no":
            print("\nThanks for playing! Goodbye.")
            playing = False
        else:
            print("\nThat wasn't yes or no, so we'll end the game here. Goodbye!")
            playing = False


if __name__ == "__main__":
    main()
