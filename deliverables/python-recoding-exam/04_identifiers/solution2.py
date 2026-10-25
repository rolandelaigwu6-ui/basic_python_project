# def next_code(codes):

def next_code(codes):
    if not isinstance(codes, list):
        raise TypeError("must be printed in list")
    
    seen = set()
    highest = 0
    for code in codes:
        if not isinstance(code, str):
            raise TypeError("Type not a string")
        
        if not code.startswith("R"):
            raise ValueError("must start with R")
        digit = code[1:]
        
        if not (digit.isascii() and digit.isdigit()):
            raise ValueError("Digit must be a valid ascii digit")
        val = int(digit)
        if val <= 0:
            raise ValueError("digit must be Positive")
        
        if f"R{val: 03d}" != code:
            raise ValueError("Invalid Padding or formatting")
        if code in seen:
            raise ValueError("The Digit Must not Containe Duplicate ID")
        seen.add(code)

        if val > highest:
            highest = val 
    return f"R{highest + 1: 03d}"
