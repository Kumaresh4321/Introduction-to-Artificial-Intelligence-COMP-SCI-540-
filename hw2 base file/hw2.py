import sys
import math


def get_parameter_vectors():
    '''
    This function parses e.txt and s.txt to get the  26-dimensional multinomial
    parameter vector (characters probabilities of English and Spanish) as
    descibed in section 1.2 of the writeup

    Returns: tuple of vectors e and s
    '''
    #Implementing vectors e,s as lists (arrays) of length 26
    #with p[0] being the probability of 'A' and so on
    e=[0]*26
    s=[0]*26

    with open('e.txt',encoding='utf-8') as f:
        for line in f:
            #strip: removes the newline character
            #split: split the string on space character
            char,prob=line.strip().split(" ")
            #ord('E') gives the ASCII (integer) value of character 'E'
            #we then subtract it from 'A' to give array index
            #This way 'A' gets index 0 and 'Z' gets index 25.
            e[ord(char)-ord('A')]=float(prob)
    f.close()

    with open('s.txt',encoding='utf-8') as f:
        for line in f:
            char,prob=line.strip().split(" ")
            s[ord(char)-ord('A')]=float(prob)
    f.close()

    return (e,s)

def shred(filename):
    #Using a dictionary here. You may change this to any data structure of
    #your choice such as lists (X=[]) etc. for the assignment
    X = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    with open (filename,encoding='utf-8') as f:
        for line in f:
            for c in line:
                c = c.upper()
                try:
                    X[c] += 1
                except KeyError:
                    a = 1
    return X

# Code Start
# Get inputs
if len(sys.argv) < 4:
    a = 1
else:
    text_file = sys.argv[1]
    eng_prior = sys.argv[2] 
    spanish_prior = sys.argv[3] 

e,s = get_parameter_vectors()   #Initialize parameters

#Q1
# Shred Text File
X = shred(text_file) 
print("Q1")                    
for i in X:
    print(i, end =" ")
    print(X[i])

#Q2
# Compute X1 log e1 and X1 log s1
q2_eng = X["A"]*math.log(e[0])
q2_spanish = X["A"]*math.log(s[0])
print("Q2")
print("{:.4f}".format(q2_eng)) 
print("{:.4f}".format(q2_spanish)) 

#Q3
# Calculating F(y)
# log f(y) = log P(Y=y)+summation[Xi * log pi]
print("Q3")
prob_eng = math.log(float(eng_prior))
temp1 = 0
holder = 0
for i in X:
    temp1 += X[i]*math.log(e[holder])
    holder += 1
F_eng = prob_eng + temp1
print("{:.4f}".format(F_eng)) 

prob_spanish = math.log(float(spanish_prior))
temp2 = 0
holder = 0
for j in X:
    temp2 += X[j]*math.log(s[holder])
    holder += 1
F_spanish = prob_spanish + temp2
print("{:.4f}".format(F_spanish)) 

#Q4
# Probability of English given Spanish
power_term = F_spanish - F_eng
if (power_term>= 100):
    print("Q4")
    probability = 0
    print("{:.4f}".format(probability)) 
elif(power_term<= -100):
    probability = 1
    print("Q4")
    print("{:.4f}".format(probability)) 
else:
    denominator = 1 + math.exp(power_term)
    probability = 1/denominator
    print("Q4")
    print("{:.4f}".format(probability)) 