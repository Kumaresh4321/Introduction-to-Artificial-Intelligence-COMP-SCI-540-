import math
# # To create a Dictionary of ASCII characters

# def create_ascii_casefold_dict_for_alphabets():
#     ascii_dict = {}
    
#     # Loop through ASCII values for alphabetic characters only
#     for i in range(65, 91):  # ASCII values for A-Z
#         char = chr(i)        # Get the uppercase character
#         folded_char = char  # Apply case folding (lowercase equivalent)
#         ascii_dict[char] = 0   # Store the casefolded char
     
#     for i in range(97, 123):  # ASCII values for a-z
#         char = chr(i)        # Get the lowercase character
#         folded_char = char.upper()  # Apply case folding (lowercase equivalent)
#         ascii_dict[char] = 0   # Store the casefolded char
    
#     return ascii_dict

# # Example usage
# ascii_casefold_dict = create_ascii_casefold_dict_for_alphabets()
# print(ascii_casefold_dict)


# Shredding
X = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
with open ("letter0.txt",encoding='utf-8') as f:
    for line in f:
        stripped = line.strip()
        for c in stripped:
            c = c.upper()
            try:
                X[c] += 1
            except KeyError:
                a = 1
#print(X)

# Calculating C(X)-multinomial coefficient
numerator = 0
denominator = 1 # since its a multiplication operation
for i in X:
    numerator += X[i]
    denominator *= math.factorial(X[i])
numerator = math.factorial(numerator)
mc = numerator/ denominator
print(numerator)
print(denominator)
print(mc)

# Calculating P(X)-multinomial coefficient
p_s = {
    'A': 0.121649,
    'B': 0.014906,
    'C': 0.0387155,
    'D': 0.0467187,
    'E': 0.140856,
    'F': 0.00690276,
    'G': 0.010004,
    'H': 0.0118047,
    'I': 0.0598239,
    'J': 0.00520208,
    'K': 0.00110044,
    'L': 0.052421,
    'M': 0.0308123,
    'N': 0.070028,
    'O': 0.0920368,
    'P': 0.0289116,
    'Q': 0.0111044,
    'R': 0.0641257,
    'S': 0.0720288,
    'T': 0.0460184,
    'U': 0.0469188,
    'V': 0.0105042,
    'W': 0.00040016,
    'X': 0.00140056,
    'Y': 0.0109044,
    'Z': 0.00470188
}
p = 1
for i in p_s:
    p *= p_s[i]**X[i]

test = X['A']*math.log(p_s['A'])

print(test)

# Calculating F(y)
# log f(y) = log P(Y=y)+summation[Xi * log pi]

prob_y = math.log(0.4)
summ = 0
for i in p_s:
    summ += X[i]*math.log(p_s[i])
F_spanish = prob_y + summ
print(F_spanish)

# Probability of English given X
