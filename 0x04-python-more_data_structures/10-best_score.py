#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    Maxi = 0
    for key, value in a_dictionary.items():
        if value > Maxi:
            Maxi = value
    for key, value in a_dictionary.items():
        if value == Maxi:
            return key
