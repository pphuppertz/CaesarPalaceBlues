def rotate_character(char, rot):

    #We want everything that is not an alphabetic character to remain unchanged. 
    if char.isalpha() == False:
        return char

    charOrd = get_character_number(char)
    
    newCharOrd = charOrd + rot

    # If we add, for instance, 5 to the character 'X', we're going to get 28, which is past the Z. 
    # That's why we want to rollover to get back to A, so effectively, we get the fifth character from X, whis is (... y... z... a... b...) C!
    # To do that, we take the mod of a division by 26... and 28 % 26 is 2, and C is indeed the charachter with number 2, so we're good. 
    if newCharOrd > 25:
        newCharOrd = newCharOrd % 26
    
    # Now we need to add what we subtracted earlier (in get_character_number) to get at the correct ordinal 
    # (the Unicode code point for the character we want to return).
    if char.isupper():
        addValue = 65
    else:
        addValue = 97
    return chr(newCharOrd + addValue)

def get_character_number(char):
    # We want the character numbering to start at zero for A or a, and to end at 25 for Z or z, in order to be able to, 
    # if our rotate value (rot) causes us to rollover to a, we can use the modulo function to get the number we need. 
    charOrd = ord(char)
    if char.isupper():
        subtractionValue = 65
    else:
        subtractionValue = 97

    return charOrd - subtractionValue

    

def main():
    print (rotate_character("U", 5))

if __name__ == "__main__":
    main()
