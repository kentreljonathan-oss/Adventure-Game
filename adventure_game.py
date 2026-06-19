import random
import json
import os

SCORES_FILE = "scores.json"


def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_score(name, score):
    scores = load_scores()
    scores.append({"name": name, "score": score})
    scores.sort(key=lambda entry: entry["score"], reverse=True)
    scores = scores[:5]
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)


def show_leaderboard():
    scores = load_scores()
    print("\n" + "=" * 50)
    print("TOP 5 HIGH SCORES")
    print("=" * 50)
    if not scores:
        print("No scores yet. Be the first to set one!")
    else:
        for i, entry in enumerate(scores, start=1):
            print(f"{i}. {entry['name']} - {entry['score']} points")
    print("=" * 50)


def show_welcome():
    print("=" * 50)
    print("WELCOME TO THE MYSTERIOUS FOREST ADVENTURE")
    print("=" * 50)
    print("You wake up at the edge of a dark forest.")
    print("Rumors say a hidden treasure lies somewhere beyond it.")
    print("Your choices and your courage in battle will decide your fate.")
    print("=" * 50)


def combat(player, enemy_name, enemy_hp, enemy_attack):
    print(f"\nA {enemy_name} appears! It has {enemy_hp} HP.")
    while enemy_hp > 0 and player["hp"] > 0:
        print(f"\nYour HP: {player['hp']}  |  {enemy_name} HP: {enemy_hp}")
        print("1. Attack")
        print("2. Defend (reduce incoming damage)")
        print("3. Try to flee")

        move = input("Choose your move (1/2/3): ")

        if move == "1":
            base_damage = random.randint(8, 15)
            if "rusty sword" in player["inventory"]:
                base_damage += 5
            enemy_hp -= base_damage
            print(f"You strike the {enemy_name} for {base_damage} damage.")
        elif move == "2":
            print("You raise your guard, ready for the next hit.")
        elif move == "3":
            chance = random.randint(1, 2)
            if chance == 1:
                print(f"You manage to escape from the {enemy_name}.")
                return "fled"
            else:
                print("You fail to escape and the enemy gets a free hit.")
        else:
            print("You hesitate, wasting your turn.")

        if enemy_hp <= 0:
            break

        incoming = random.randint(enemy_attack - 3, enemy_attack + 3)
        if move == "2":
            incoming = max(0, incoming - 8)
        if "wooden shield" in player["inventory"] and move != "2":
            incoming = max(0, incoming - 3)
        player["hp"] -= incoming
        print(f"The {enemy_name} hits you for {incoming} damage.")

    if player["hp"] <= 0:
        return "defeated"
    return "won"


def chapter_one_forest(player):
    print("\n--- CHAPTER 1: THE FOREST PATH ---")
    print("You are standing at a fork in the path.")
    print("1. Enter the dark forest")
    print("2. Walk along the river")
    print("3. Climb the rocky hill")

    choice = input("What do you choose? (1/2/3): ")

    if choice == "1":
        print("\nYou step into the forest and find an old rusty sword.")
        player["inventory"].append("rusty sword")
        player["score"] += 10
    elif choice == "2":
        print("\nYou walk along the river and find a shiny coin.")
        player["inventory"].append("shiny coin")
        player["score"] += 5
    elif choice == "3":
        print("\nYou climb the hill and find a sturdy wooden shield.")
        player["inventory"].append("wooden shield")
        player["score"] += 10
    else:
        print("\nYou hesitate and the path disappears into mist.")
        player["score"] -= 5

    print(f"\nInventory: {player['inventory']}")
    print(f"HP: {player['hp']}  |  Score: {player['score']}")

    result = combat(player, "goblin", enemy_hp=30, enemy_attack=10)

    if result == "defeated":
        print("\nThe goblin overwhelms you. Your journey ends here.")
        return False
    elif result == "fled":
        print("\nYou slip away into the trees, shaken but alive.")
        player["score"] += 5
    else:
        print("\nYou defeat the goblin and press onward.")
        player["score"] += 20

    return True


def chapter_two_village(player):
    print("\n--- CHAPTER 2: THE ABANDONED VILLAGE ---")
    print("You emerge from the forest into a quiet, abandoned village.")
    print("An old merchant sits alone by a fire.")
    print("1. Trade an item with the merchant")
    print("2. Search the empty houses")
    print("3. Ignore the village and keep moving")

    choice = input("What do you choose? (1/2/3): ")

    if choice == "1":
        if player["inventory"]:
            item = player["inventory"].pop()
            print(f"\nYou trade your {item} for a healing potion.")
            player["inventory"].append("healing potion")
            player["hp"] = min(100, player["hp"] + 20)
            player["score"] += 10
        else:
            print("\nYou have nothing to trade. The merchant waves you off.")
    elif choice == "2":
        chance = random.randint(1, 3)
        if chance == 1:
            print("\nYou find a hidden stash of gold!")
            player["score"] += 25
        elif chance == 2:
            print("\nA loose floorboard snaps and you twist your ankle.")
            player["hp"] -= 10
        else:
            print("\nThe houses are empty. You find nothing of value.")
    elif choice == "3":
        print("\nYou keep your distance and continue on your way.")
    else:
        print("\nYou freeze, unsure what to do, and waste valuable time.")
        player["score"] -= 5

    print(f"\nInventory: {player['inventory']}")
    print(f"HP: {player['hp']}  |  Score: {player['score']}")

    if player["hp"] <= 0:
        print("\nYour wounds catch up with you. Your journey ends here.")
        return False

    print("\nA pack of wild wolves surrounds you as you try to leave!")
    result = combat(player, "wolf pack", enemy_hp=40, enemy_attack=12)

    if result == "defeated":
        print("\nThe wolves prove too much for you. Your journey ends here.")
        return False
    elif result == "fled":
        print("\nYou break free and keep moving, breathing hard.")
        player["score"] += 5
    else:
        print("\nYou fight off the wolves and continue toward the mountain.")
        player["score"] += 25

    return True


def chapter_three_cave(player):
    print("\n--- CHAPTER 3: THE GLOWING CAVE ---")
    print("You reach a glowing cave at the base of the mountain.")
    print("This could be where the treasure is hidden.")
    print("1. Enter the cave carefully")
    print("2. Rush in without thinking")
    print("3. Turn back home")

    choice = input("What do you choose? (1/2/3): ")

    if choice == "3":
        print("\nYou decide the journey is too dangerous and head home safely.")
        print("ENDING: SAFE BUT EMPTY HANDED")
        return

    if choice == "2":
        print("\nYou charge in and a cave guardian notices you immediately.")
        player["score"] -= 5
    elif choice == "1":
        print("\nYou step in carefully, watching for traps.")
    else:
        print("\nYou stand still too long and the cave entrance begins to seal.")
        player["score"] -= 5

    print("\nA cave guardian made of stone rises to block your path!")
    result = combat(player, "cave guardian", enemy_hp=55, enemy_attack=15)

    if result == "defeated":
        print("\nThe guardian proves too strong. Your journey ends here.")
        print("ENDING: DEFEATED IN THE DEPTHS")
        return
    elif result == "fled":
        print("\nYou escape the cave, treasure just out of reach.")
        print("ENDING: ESCAPED EMPTY HANDED")
        return

    player["score"] += 30

    if player["score"] >= 80:
        print("\nWith the guardian defeated, you find a chest overflowing with gold!")
        print("ENDING: TREASURE HUNTER VICTORY")
    else:
        print("\nYou find a small pile of coins, modest but hard earned.")
        print("ENDING: MODEST FORTUNE")


def play_game():
    player = {
        "inventory": [],
        "score": 0,
        "hp": 100
    }

    show_welcome()

    if not chapter_one_forest(player):
        return player["score"]

    if player["hp"] <= 0:
        return player["score"]

    if not chapter_two_village(player):
        return player["score"]

    if player["hp"] <= 0:
        return player["score"]

    chapter_three_cave(player)

    print(f"\nFinal inventory: {player['inventory']}")
    print(f"Final score: {player['score']}")
    print("=" * 50)

    return player["score"]


def main():
    show_leaderboard()

    playing = True
    while playing:
        final_score = play_game()

        name = input("\nEnter your name for the leaderboard: ").strip()
        if not name:
            name = "Adventurer"
        save_score(name, final_score)
        show_leaderboard()

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