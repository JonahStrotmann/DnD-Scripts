import random, sys, getopt, os, time

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

#Don't save anything generated to a file
save = False

#verbose output -> show all rolls
verbose = False

#location of the output file
output = ''

#Commandline arguments v: verbose o: save to path
opts, rest = getopt.getopt(sys.argv[1:], "vo:")

for opt, arg in opts:
    if opt == '-v':
        verbose = True
    if opt == '-o':
        save = True
        output = arg
    
#file to save the information in if saving is enabled
if (save):
    if(os.path.exists(output)):
        print("File already exists! Proceeding without saving to a file")
        time.sleep(3)
        save = False
    else:
        outputfile = open(output, 'w')
    


for i in range(6):
    random_numbers = []

    for i in range(4):
        random_numbers.append(random.randint(1, 6))
    
    if(verbose):
        print("lowest number: " + str(random_numbers[random_numbers.index(min(random_numbers))]))
    del random_numbers[random_numbers.index(min(random_numbers))]

    #get the total value
    total_value = 0

    for i in range(len(random_numbers)):
        if(verbose): 
            print(str(i+1) + ". " + str(random_numbers[i]))
        total_value += random_numbers[i]
    
    if(verbose):
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
    if(save):
        outputfile.write(str(i+1) + ": " + str(values[i]) + "  modifier: " + str(modifier) + "\n")