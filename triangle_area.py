#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program calculates the area of a triangle with a function


def calculate_area(height, base):
    # This function calculates the area

    # Process
    area = (height * base) / 2

    # Output
    print("")
    print("The area is {} cm².".format(area))
    print("\nDone.")


def main():
    # This function gets the height and base lengths

    # Input
    print("This program calculates the area of a triangle.")
    print("")
    height_input_string = input("Enter the height of the triangle (cm): ")
    base_input_string = input("Enter the length of the base (cm): ")

    # Process
    while True:
        try:
            height_input_integer = int(height_input_string)

            if height_input_integer > 0:
                break
            else:
                height_input_string = input("Must be a positive integer. "
                                            "Enter the height of the "
                                            "triangle (cm): ")
        except Exception:
            height_input_string = input("{} is not a valid input. Enter the "
                                        "height (cm): ".
                                        format(height_input_string))
    while True:
        try:
            base_input_integer = int(base_input_string)

            if base_input_integer > 0:
                break
            else:
                base_input_string = input("Must be a positive integer. Enter "
                                          "the length of the base (cm): ")
        except Exception:
            base_input_string = input("{} is not a valid input. Enter the "
                                      "length of the base (cm): ".
                                      format(base_input_string))

    # Call functions
    calculate_area(height_input_integer, base_input_integer)


if __name__ == "__main__":
    main()
