
def anagrams(str_1, str_2):
    """
    function to test if two  strings are anagrams or not


    """
    s1 = ''.join(char.lower() for char in str_1 if char.isalnum())
    s2 = ''.join(char.lower() for char in str_2 if char.isalnum())
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False