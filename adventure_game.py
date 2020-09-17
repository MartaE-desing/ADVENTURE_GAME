import time
import random
import sys

items = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro(country):
    print_pause("You are at home having a good time with your family.")
    print_pause("Suddenly the ring bells, Its your commander.")
    print_pause("He tells you that you have to go to " +
                country + " on a military mission.")
    print_pause("After a long trip, you find yourself in " + country + " and "
                " you are on a dangerous zone "
                " surrounded by enemies "
                " Which place would you choose to hide?.")
    go_somewhere()


def first_house():
    print_pause("You go to the house.")
    print_pause("You look on the first floor, to "
                " find something that can be useful.")

    if "toolbox" in items:
        print_pause("There is nothing more in the house.")

    else:
        print_pause("You have found a toolbox behind the closet.")
        items.append("toolbox")
    print_pause("You can go out, there "
                " is nothing more to do here.")
    go_somewhere()


def second_rock():
    print_pause("You are ouside but there are enemies everywhere")
    print_pause("You see a rock, that "
                "is a good place to cover up")
    if "key" in items:
        print_pause("Someone is aproaching you,"
                    "you cannot longer hide in here")

    else:
        print_pause("You are safe now¡")
        if "toolbox" in items:
            print_pause("You see something shiny on the floor. "
                        "It looks "
                        "like the key for the tank")
            items.append("key")
        else:
            print_pause("To open the tank you need to get a toolbox first")

    go_somewhere()


def third_tank():
    print_pause("You approach to the tank")

    if "toolbox" and "key" not in items:
        print_pause("You are not ready to start the tank")
        go_somewhere()
    elif "toolbox" and "key" in items:
        print_pause("You open the tank´s door with the key "
                    " and use your toolbox to fix the circuit")
        activate = False
        while(activate is False):
            print_pause("You see two buttons red and green "
                        ", Which one would you like to press?")
            option = input("1. red\n"
                           "2. green")
            if option == "2":
                activate = True
                print_pause("The tank is working. you can help the troop.")
                final_option()

            if option == "1":
                activate = False
                print_pause("The tank is not working.")


def final_option():
    print_pause("There are two ways, Which way do you choose??")
    option = input("1. Left\n"
                   "2. Right")
    if option == "1":
        print_pause("There is a cliff, You fall into the cliff and die.")
        play_again()

    elif option == "2":
        print_pause("There is your troop, you can help "
                    " them to fight the enemy. You are a HERO¡¡")
        play_again()

    else:
        final_option()


def go_somewhere():
    print_pause("Please enter the number for the "
                " place you would like to go ")
    place = input("1. On a house\n"
                  "2. Behind a rock\n"
                  "3. Inside the tank\n")
    if place == "1":
        first_house()
    elif place == '2':
        second_rock()
    elif place == '3':
        third_tank()
    else:
        go_somewhere()


def play_again():
    again = input("Would you like yo play again? (y/n)").lower()
    if again == "y":
        print_pause("Perfect¡ Restarting the game ...")
        play_game()
    elif again == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        go_somewhere()


def play_game():
    country = random.choice(["Afganistan", "Irak", "Siria"])
    intro(country)


play_game()
