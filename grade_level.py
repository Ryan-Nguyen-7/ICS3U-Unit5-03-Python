#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on January 2021
# This program uses a function to convert
#   a grade level into a percentage


def calculate_percentage(grade_level):
    # converts grade level to perentage grade

    # process
    if grade_level == "r":
        grade_percentage = 25
    elif grade_level == "1-":
        grade_percentage = 51
    elif grade_level == "1":
        grade_percentage = 55
    elif grade_level == "1+":
        grade_percentage = 58
    elif grade_level == "2-":
        grade_percentage = 61
    elif grade_level == "2":
        grade_percentage = 65
    elif grade_level == "2+":
        grade_percentage = 68
    elif grade_level == "3-":
        grade_percentage = 71
    elif grade_level == "3":
        grade_percentage = 75
    elif grade_level == "3+":
        grade_percentage = 78
    elif grade_level == "4-":
        grade_percentage = 83
    elif grade_level == "4":
        grade_percentage = 91
    elif grade_level == "4+":
        grade_percentage = 97
    else:
        grade_percentage = -1

    return grade_percentage


def main():
    # input
    grade_level = input("Enter grade level: ")
    print("")

    # call function
    grade_percentage = calculate_percentage(grade_level)

    # output
    if grade_percentage == -1:
        print("Invalid integer")
    else:
        print("Percentage grade: {}".format(grade_percentage))


if __name__ == "__main__":
    main()
