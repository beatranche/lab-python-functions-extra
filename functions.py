def f_get_unique_list(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.

    Parameters:
    lst (list): The input list.

    Returns:
    list: A new list with unique elements from the input list.
    """
    list_set = set(lst)
    unique_list = list(list_set)
    return unique_list

def f_count_case(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.

    Parameters:
    string (str): The string to count uppercase and lowercase letters in.

    Returns:
    A tuple containing the count of uppercase and lowercase letters in the string.
    """
    count_upper = 0
    count_lower = 0
        
    for character in string:
        if character in string.upper():
            count_upper += 1
        elif character in string.lower():
            count_lower += 1
    
    tuple_count = ('Uppercase:', count_upper, 'Lowercase:', count_lower)
    
    return tuple_count 


def f_remove_punctuation(sentence):
    import string
    """
    Removes all punctuation marks (commas, periods, exclamation marks, question marks) from a sentence.

    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    str: The sentence without any punctuation marks.
    """
    
    return sentence.translate(str.maketrans('', '', string.punctuation))

def f_word_count(sentence):
    """
    Counts the number of words in a given sentence. To do this properly, first it removes punctuation from the sentence.
    Note: A word is defined as a sequence of characters separated by spaces. We can assume that there will be no leading or trailing spaces in the input sentence.
    
    Parameters:
    sentence (str): A string representing a sentence.

    Returns:
    int: The number of words in the sentence.
    """
    return len(f_remove_punctuation(sentence).split())