import pandas as pd

def validate(n, nn, rule):
    #print(f"Validating: {n} vs {nn}")
    #print(f"Rule: {rule[0]} must precede {rule[1]}")
    if n==rule[1] and nn==rule[0]:
        print(f"Validating: {n} vs {nn}")
        print(f"Rule: {rule[0]} must precede {rule[1]}")
        return False
    else:
        return True

def evaluate_line(line_to_validate, rules):
    for x in range(len(line_to_validate)):     # loop pairs in the list 
        for y in range(len(line_to_validate)): # check all pairs
            for _, rule in rules.iterrows():   # iterate over rules
                if y > x and not(validate(line_to_validate[x], line_to_validate[y], rule)):
                    return 0
    return line_to_validate[len(line_to_validate)//2]
               
rules = pd.read_csv('rules.txt', sep='|')

print("Rules:")
print(rules)
count = 0

l = [44, 37, 22, 85, 54]
#print(evaluate_line(line.strip().split(','), rules))
with open('text_to_evaluate.txt', 'r') as file:
    for line in file:
        values = line.strip().split(',') 
        values2 = list(map(lambda x: int(x.strip()), values))
        #print(evaluate_line(values2, rules))
        count +=  evaluate_line(values2, rules)
print(f"{count}")
            
