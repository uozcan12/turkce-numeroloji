import math
from collections import Counter
from typing import Dict, Tuple
  
# For Turkish Character
translation_table = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")

pick_topic = {
    "1": "activity, addiction, individuality",
    "2": "diplomacy, harmony, cooperation",
    "3": "joy, creativity, words",
    "4": "patience, service, building",
    "5": "experience, strangers, change",
    "6": "responsibility, home, love",
    "7": "philosophy, analysis, retreat, waiting",
    "8": "authority, success, growth",
    "9": "sympathy, disappointment, compassion, greatness"
}


alphabet = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 1,
    "k": 2,
    "l": 3,
    "m": 4,
    "n": 5,
    "o": 6,
    "p": 7,
    "q": 8,
    "r": 9,
    "s": 1,
    "t": 2,
    "u": 3,
    "v": 4,
    "w": 5,
    "x": 6,
    "y": 7,
    "z": 8,
}

first_name = "Uğur"
last_name = "Özcan"
birthday = "1993-01-20"
first_name_cleaned = first_name.lower().translate(translation_table)
last_name_cleaned = last_name.lower().translate(translation_table)

        

def match_numbers_to_letters(string: str, alphabet: Dict) -> Tuple[int]:
    if string:
        return tuple(alphabet[letter] for letter in string)
    else:
        return None

def full_name_numbers(first_name_cleaned, last_name_cleaned, alphabet) -> Dict[int, int]:
    """Returns the numbers from the full name as a dict(Counter).
    The dict contains the numbers and their occurrences."""
    full_name = first_name_cleaned + last_name_cleaned
    full_name_num = match_numbers_to_letters(full_name, alphabet)
    full_name_counter = Counter(full_name_num).most_common()
    full_name_counter_dict = dict(full_name_counter)
    return full_name_counter_dict

def full_name_missing_numbers(first_name_cleaned, last_name_cleaned, alphabet):
    """Returns the missing numbers from the name as a tuple."""
    full_name = first_name_cleaned + last_name_cleaned
    full_name_num = match_numbers_to_letters(full_name, alphabet)
    return list([number for number in range(1, 10) if number not in full_name_num])

def first_pick_age_and_status(birthday):
    """Returns the first pick age in life period and effect"""
    accepted_number = [1,2,3,4,5,6,7,8,9,11,22]
    sum_of_digits = sum(int(x) for x in birthday if x.isdigit())
    if sum_of_digits not in accepted_number:
        sum_of_digits = sum(int(x) for x in str(sum_of_digits) if x.isdigit())
        
    first_pick_age = 36 - sum_of_digits
    
    year, month, day = birthday.split("-")
    sum_of_day_digits = sum(int(x) for x in day if x.isdigit()) 
    sum_of_month_digits = sum(int(x) for x in month if x.isdigit()) 
    pick_topic_digit = sum_of_day_digits + sum_of_month_digits
    
    if pick_topic_digit not in accepted_number:
        pick_topic_digit = sum(int(x) for x in str(pick_topic_digit) if x.isdigit())
    
    return [first_pick_age, pick_topic[str(pick_topic_digit)]]  

def second_pick_age_and_status():
    """Returns the second pick age in life period and effect"""
    first_pick_age = first_pick_age_and_status(birthday)[0]
    return first_pick_age + 9

def third_pick_age_and_status():
    """Returns the third pick age in life period and effect"""
    second_pick_age = second_pick_age_and_status()
    return second_pick_age + 9

def fourth_pick_age_and_status():
    """Returns the fourth pick age in life period and effect"""
    third_pick_age = third_pick_age_and_status()
    return third_pick_age + 9    


return_object = {
    "first_name": first_name,
    "last_name": last_name,
    "full_name_numbers": full_name_numbers(first_name_cleaned, last_name_cleaned, alphabet),
    "full_name_missing_numbers": full_name_missing_numbers(first_name_cleaned, last_name_cleaned, alphabet),
    "first_pick_age": first_pick_age_and_status(birthday)[0],
    "first_pick_topic": first_pick_age_and_status(birthday)[1],
    "second_pick_age": second_pick_age_and_status(),
    "third_pick_age": third_pick_age_and_status(),
    "fourth_pick_age": fourth_pick_age_and_status()
}

print(return_object)



"""
TARGET -->
{
    "first_name": "Barack",
    "last_name": "Obama",
    "birthdate": "1961-08-04",
    "life_path_number": 2,
    "life_path_number_alternative": 2,
    "hearth_desire_number": 1,
    "personality_number": 22,
    "destiny_number": 5,
    "expression_number": 5,
    "birthdate_day_num": 4,
    "birthdate_month_num": 8,
    "birthdate_year_num": 8,
    "birthdate_year_num_alternative": 7,
    "active_number": 9,
    "legacy_number": 5,
    "power_number": 7,
    "power_number_alternative": 7,
    "full_name_numbers": {
        "1": 4,
        "2": 3,
        "9": 1,
        "3": 1,
        "6": 1,
        "4": 1
    },
    "full_name_missing_numbers": [
        5,
        7,
        8
    ]
}
"""

