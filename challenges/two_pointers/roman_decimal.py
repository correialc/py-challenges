def roman_decimal_decode(roman: str) -> int:

    # Vocabulary for roman numbers
    translator: dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Pointers to navigate through the Roman number 
    cur: int = 0
    nxt: int = 1
    
    # Size of the roman number (used for navigation)
    roman_size: int = len(roman)
    
    # Converted decimal number
    decimal: int = translator[roman[cur]]
    
    # Special case: 1 digit roman number (no further navigation needed)
    if roman_size == 1:
        return decimal
        
    while (nxt < roman_size):
        
        if translator[roman[cur]] < translator[roman[nxt]]:
            decimal = decimal - translator[roman[cur]] + (translator[roman[nxt]] - translator[roman[cur]])
        else:
            decimal += translator[roman[nxt]]
                
        cur += 1
        nxt += 1
    
    return decimal
     