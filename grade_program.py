#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 05, 19, 2025
# This program calculates mark.

import random


def mark(user_input):
    # Matches the user output with the correct mark and then returns it to def main
    match user_input:
        case "4+":
            mark_2 = 98
            return mark_2
        case "4":
            mark_2 = 85
            return mark_2
        case "4-":
            mark_2 = 82
            return mark_2
        case "3+":
            mark_2 = 78
            return mark_2
        case "3":
            mark_2 = 75
            return mark_2
        case "3-":
            mark_2 = 72
            return mark_2
        case "2+":
            mark_2 = 67
            return mark_2
        case "2":
            mark_2 = 64
            return mark_2
        case "2-":
            mark_2 = 62
            return mark_2
        case "1+":
            mark_2 = 59
            return mark_2
        case "1":
            mark_2 = 56
            return mark_2
        case "1-":
            mark_2 = 53
            return mark_2
        case "NE":
            # Creates random number from 0 to 50 and also returns it as in all statements before
            mark_2 = random.randint(0, 50)
            return mark_2


def main():
    # Gets input from user
    user_input = input("Insert the mark.")
    # checks user on correct input
    if (
        user_input == "4+"
        or "4"
        or "4-"
        or "3+"
        or "3"
        or "3-"
        or "2+"
        or "2"
        or "2-"
        or "1+"
        or "1"
        or "1-"
        or "NE"
    ):
        # Calls the function
        mark_2 = mark(user_input)
        print(f"Your mark is, {mark_2}")
        # Displays message if user got incorrect input
    else:
        print("Your mark is, None")


if __name__ == "__main__":
    main()
