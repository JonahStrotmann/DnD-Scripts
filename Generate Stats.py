import random, sys, getopt

values = []
#define hashmap for the modifiers
modifiers = {
    '1' : -5,
    '2' : -4,
    '4' : -3,
    '6' : -2,
    '8' : -1,
    '10' : 0,
    '12' : 1,
    '14' : 2,
    '16' : 3,
    '18' : 4,
    '20' : 5,
    '22' : 6,
    '24' : 7,
    '26' : 8,
    '28' : 9,
    '30' : 10
}
#file to save the information in
outputfile = open()


for i in range(6):
    random_numbers = []

    for i in range(4):
        random_numbers.append(random.randint(1, 6))

    print("lowest number: " + str(random_numbers[random_numbers.index(min(random_numbers))]))
    del random_numbers[random_numbers.index(min(random_numbers))]

    #get the total value
    total_value = 0

    for i in range(len(random_numbers)):
        print(str(i+1) + ". " + str(random_numbers[i]))
        total_value += random_numbers[i]
    print("Total: " + str(total_value) + "\n")
    values.append(total_value)

print("\n\nNumbers:")
for i in range(len(values)):  
    #get modifier
    modifier = 0
    if(values[i] % 2 != 0):
        modifier = modifiers[str(values[i]-1)]
    else:
        modifier = modifiers[str(values[i])]
    
    print(str(i+1) + ": " + str(values[i]) + "  modifier: " + str(modifier))
