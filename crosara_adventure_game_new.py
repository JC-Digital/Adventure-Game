# Author: Julia Crosara
# Project 2: Aventure Game: Art Heist of the Century
# Submitted June 9, 2019
#
# Please note: some of the content for the storyline came from Wikipedia
# Source: https://en.wikipedia.org/wiki/Vincenzo_Peruggia


import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(3)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower().strip()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, that is not an option.")
    return response


def intro():
    print_pause("It's 1911 and you are an Italian art thief in Paris.")
    print_pause("You are attempting to steal the most famous painting\n"
                "in the world, the Mona Lisa.")
    print_pause("You are driven by the belief that DaVinci's masterpiece\n"
                "belongs in Italy.")
    print_pause("You are willing to risk it all to bring her back to her\n"
                "rightful home.")
    print_pause("To prepare for the heist, you get a job at the Louvre to\n"
                "understand how the museum operates.")


def enter_museum():
    print_pause("At 7:00am on Aug 21, you put on your work uniform\n"
                "and enter the museum from a staff entrance.")
    print_pause("You see someone you work with walking towards you.")
    see_someone()


def see_someone():
    choice = input("What do you do next? Enter 1 or 2.\n"
                   "1. Duck into a storage closet.\n"
                   "2. Turn and walk the other way.\n")

    if choice == '1':
        print_pause("The closet is full of supplies. You look around for\n"
                    "something that might be of use.")
        take_supplies()

    elif choice == '2':
        print_pause("You step into the staff lounge and see an extra\n"
                    "large uniform hanging on a hook. You change into it\n"
                    "and leave the other one behind.")
        print_pause("You walk to the room where the painting is hung.")
        remove_painting()
        print_pause("You slip the painting inside the baggy uniform,\n"
                    "head back the way you came and walk out the door.")
        print_pause("Trembling with excitement, you have visions of\n"
                    "being a national hero in Italy!")
        print_pause("Suddenly, you are surrounded by French policemen.")
        print_pause("They toss you in jail and throw away the key.")
        print_pause("Game over!")
        play_again()

    else:
        print_pause("Sorry, that is not an option.")
        see_someone()


def take_supplies():
    supplies = ["drop cloth", "wooden crate", "screwdriver"]
    supply = random.choice(supplies)
    print_pause("You grab a " + supply + ", exit the closet,\n"
                "and walk straight to the painting.")

    if supply == "drop cloth":
        remove_painting()
        print_pause("You cover the painting with the drop cloth, secure it\n"
                    "under your arm, and take the stairs to the lower level.")
        print_pause("After walking through a maze of hallways, you see a\n"
                    "door on your left and another on your right.")
        choose_door()

    elif supply == "wooden crate":
        remove_painting()
        print_pause("The crate has packing material inside. You cover\n"
                    "up the painting and place it in the crate.")
        print_pause("The crate is heavier than expected so you push it\n"
                    "along the floor.")
        print_pause("Before you know what's happening, someone from the\n"
                    "shipping department takes the crate, throws it onto\n"
                    "the back of a truck and drives off.")
        print_pause("You yell out to the driver, telling him to stop,\n"
                    "but he keeps going.")
        print_pause("The Mona Lisa is gone. Game over.")
        play_again()

    elif supply == "screwdriver":
        remove_painting()
        print_pause("You take off your uniform, cover the painting, tuck\n"
                    "it under your arm, and run to the nearest exit.")
        print_pause("Finding the door locked, you use the tiny screwdriver\n"
                    "to pick the lock. You hear footsteps, turn around, and\n"
                    "see a maintenance worker approaching from behind.")
        print_pause("You hide the screwdriver and try to act natural.")
        print_pause("He offers to help and opens the door with his key.")
        print_pause("You walk out of the museum and into the busy street.")
        print_pause("Congratulations!! You stole the Mona Lisa! You win!")
        play_again()


def remove_painting():
    print_pause("Standing just inches from her enigmatic smile takes\n"
                "your breath away every time.")
    print_pause("You look around to make sure you're alone.")
    print_pause("You lift the painting from the wall and remove the\n"
                "protective casing and frame.")


def choose_door():
    door = input("Which one do you choose? Enter 1 or 2.\n"
                 "1. Left door\n"
                 "2. Right door\n")
    if door == '1':
        print_pause("You open the door and see a group of security guards\n"
                    "having a meeting. You run away quickly but they\n"
                    "catch up and tackle you in the hallway.")
        print_pause("They take back the painting and throw you in jail.")
        print_pause("Game Over.")
        play_again()

    elif door == '2':
        print_pause("The door opens onto an alley and you see that the\n"
                    "train station is just a few minutes away.")
        print_pause("You hop on a train and head home to Italy with your\n"
                    "pride and joy. Congratulations! You won!")
        play_again()

    else:
        print_pause("Sorry, that is not an option.")
        choose_door()


def play_again():
    response = valid_input("Would you like to play again? "
                           "Please type 'yes' or 'no'.\n",
                           "yes", "no")
    if "yes" in response:
        play_game()
    elif "no" in response:
        print_pause("OK, goodbye!")
    else:
        print_pause("Sorry, that is not an option.")
        play_again()


def play_game():
    intro()
    enter_museum()


play_game()
