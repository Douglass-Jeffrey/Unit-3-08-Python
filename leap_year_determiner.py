#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program determines if a user inputted year is a leap year


def main():

    # variables
    leap_year = " is not"

    # process
    # input
    useryear = int(input("Enter a year of your choice:"))
    print("")

    # Output
    if useryear % 4 == 0:
        if useryear % 100 == 0:
            if useryear % 400 == 0:
                leap_year = " is"
        else:
            leap_year = " is"

    print(str(useryear) + leap_year + " a leap year.")


if __name__ == "__main__":
    main()
