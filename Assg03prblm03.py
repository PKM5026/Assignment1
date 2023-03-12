# python code for upper and lower case counting.

def string_count(s):
    upper_letters = 0
    lower_letters = 0
    for char in s:
        if char.isupper():
            upper_letters += 1
        elif char.islower():
            lower_letters += 1
    print("number of upper letters is :", upper_letters)
    print("number of lower letters is :", lower_letters)

string_count("The quick Brow Fox")
