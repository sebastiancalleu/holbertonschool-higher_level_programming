#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return (0)
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum = 0
    for i in range(0, len(roman_string)):
        if (i + 1 < len(roman_string)):
            if (roman_dictionary[roman_string[i]] >= roman_dictionary[roman_string[i + 1]]):
                sum += roman_dictionary[roman_string[i]]
            else:
                sum -= roman_dictionary[roman_string[i]]
        else:
            sum += roman_dictionary[roman_string[i]]
    return (sum)
