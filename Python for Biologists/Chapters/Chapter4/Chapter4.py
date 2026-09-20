dna_bases = ['A', 'T', 'C', 'G']
base1 = dna_bases[0]
print(dna_bases[3])  # Output: G
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
print(alphabets[0])  # Output: A
print(alphabets[-1])  # Output: M
print(alphabets.index('D'))
print(alphabets[4:6])  # Output: ['E', 'F'] ,that is 4 and 5 remember the last index is not included
pets = ['dog', 'cat', 'parrot', 'hamster']
pets.append('fish')
print(pets)  # Output: ['dog', 'cat', 'parrot', 'hamster', 'fish']
print(pets[-1])
#lists as we can see behave like strings
wild = ['lion', 'croc', 'snake', 'tiger']
print(pets + wild)  # Output: ['dog', 'cat', 'parrot', 'hamster', 'fish', 'lion', 'croc', 'snake', 'tiger']
#but we can't cocantenate string to list just as we can just cocantenate int to strings
print(len(pets)) # Output: 5
#If we want to add elements from a list onto the end of an existing list, changing it in the process, we can use the extend method. extend behaves like append but takes a list as its argument rather than a single element.
pets.extend(wild)
print('animals: ' + str(pets)) # Output: ['dog', 'cat', 'parrot', 'hamster', 'fish', 'lion', 'croc', 'snake', 'tiger']
#to cocantenate a string to a list we str(list)
print('wild animals: ' + str(wild))

#By default, Python sorts strings in alphabetical order and numbers in ascending numerical order

print('at the start: ' + str(pets)) #Output: ['dog', 'cat', 'parrot', 'hamster', 'fish', 'lion', 'croc', 'snake', 'tiger']

pets.reverse()
print('after reverse: ' + str(pets)) #Output: ['tiger', 'snake', 'croc', 'lion', 'fish', 'hamster', 'parrot', 'cat', 'dog']

pets.sort()
print('after sort: ' + str(pets)) #Output: ['cat', 'croc', 'dog', 'fish', '

#Writng a loop to print all the elements of a list
animals = pets
for animal in animals:
    print(animal + " is a animal")
#Let's take a moment to look at the different parts of this loop. We start by writing for x in y, where y is the name of the list we want to process and x is the name we want to use for the current element each time round the loop. x is just a variable name (so it follows all the rules that we've already learned about variable names), but it behaves slightly differently to all the other variables we've seen so far. In all previous examples, we create a variable and store something in it, and then the value of that variable doesn't change unless we change it ourselves. Incontrast, when we create a variable to be used in a loop, we don't set its value – the value of the variable will be automatically set to each element of the list in turn, and it will be different each time round the loop. Importantly, the loop variable x only exists inside the loop – it gets created at the start of each loop iteration, and disappears at the end. This means that once the loop has finished running for the last time, that variable is gone forever. When a variable is restricted to a block of code like this, we call it the variable's scope 

apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
for ape in apes:
    name_length = len(ape)
    first_letter = ape[0]
    print(ape + " is an ape. Its name starts with " + first_letter)
    print("Its name has " + str(name_length) + " letters")

#treating a string like a list
name = 'EMMANUEL' #it treats the string "EMMANUEL" as [E,M,M,A,N,U,E,L,]
for letter in name:
    num = name.index(letter)
    print(letter  + " it is the " + str(num) + " character") 



ink='ergerg,rgr,tyjtj,fhjtg'
m=ink.split(',')
print(str(m))

jo = open("test.txt","w")
ke = jo.write("line one\nline two")
jo.close()
jo = open("test.txt")
ke = jo.read()
for dot in ke:
    print(dot)#since its treating the test file as a list which contains [l,i,n,e,  ,o,n,e, , ,l,i,n,e, ,t,w,o]#so dot stands for each charactr in the list
jo.close()

myfile = open("try.txt",'w')
files = myfile.write("trying something\nanother line")
myfile.close()#the second code would have still functioned without the close() but it is a good practice to close the file after writing to it
myfile = open("try.txt","r")# for read you dont neccessarily have to specify the mode ("r")as it is the default mode
files = myfile.read()
print(files)
myfile.close()

#Looping with ranges
protein = "vlspadktnv" 
print(str(len(protein))) #Output; 10
#we want to print an a few amino acids from the protein primary structure 
stop_positions = [3,4,5,6,7,8,9]
for stop in stop_positions:
    substring = protein[0:stop]
    print(substring)
#This is a bit cumbesome and requires us to know the length of the string ,hence i printed out the legth first and then we need to create a variable for the stop_positions which is all tiresome
#instead we use range
for number in range(6):
    print(number) #Outout: 0,1,2,3,4,5 ;remember python is non inclusive at the end

for number in range(3, 8):
    print(number)

print('\n')
#With three numbers, range will count up from the first to the second with the gap dictated by the 3rd
for dot in range(1,10,2):
    print(dot) #Output: 1,3,5,7,9

#wait so what if it started from (0,10,2) meaning the last number is supposed to be 10 ,but 10 is non inclusive ,lets see what will happen

for it in range(0,10,2):
    print(it) #Output: 0,2,4,6,8

print('\n')
doc = "AGTACGACTAACATCCCAGTACGAAGGTTTTAGTAGT"
point = range (4,44,4)#i dunno the lenght hence used a large number
print(str(len(doc))) #Output: 31 it seems if the 2nd number is larger than the length of the string ,this code repeats the last substring till the 40 quota has reached ,dunno why ,for example with this code im supposed to get 8 or 7
for num in point:
    sub = doc[:num]
    print(sub + ' ' + str(num))
