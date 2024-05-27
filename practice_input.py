"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""


def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    # write your code here.
    favorite_vegetable = input("What's your favorite vegetable? ")

    output_message = "Interesting! I also like " + favorite_vegetable + "!"

    print(output_message)


def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    # write your code here.
    favorite_number = input("What's your favorite number? ")

    start = "Interesting! I also like "
    end = "!"
    output_message = start + favorite_number + end

    print(output_message)


def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    # write your code here.
    user_name = input("What's your name? ")

    user_zodiac_sign = input("What's your zodiac sign? ")

    start = "Interesting! My name is also " + user_name + ", "
    end = "and I'm also a "+ user_zodiac_sign + "!"
    output_message = start + end

    print(output_message)


def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    # write your code here.
    user_name = input("What's your name? ")

    user_age = input("How old are you? ")

    output_message = "Interesting! My name is also " + user_name + ", " + "and I'm also " + user_age + " years old" + "!"

    print(output_message)
    