def TransToUppercase(TransData):
    converted_string = ''

    for character in TransData:
        
        if character.islower():
            character = character.upper()
        
        elif character.isdigit():
            character = str(int(character))
            
        converted_string += character
        
    return converted_string
        