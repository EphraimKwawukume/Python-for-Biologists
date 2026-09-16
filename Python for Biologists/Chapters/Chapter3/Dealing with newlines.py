my_file = open("dna.txt")
my_dna = my_file.read()
dna_length = len(my_dna)
print("sequence is "+my_dna+" and length is "+str(dna_length))
#this prints as:
#sequence is ACTGTACGTGCACTGATC 
# and length is 19  ....two lines which is not what we want and occurs due to the dna.txt having the cursor on the next line so to python this looks like \n ..and also the bases we have are 18 but it added the line making it 19 ......so we could go into the dna.txt and backspace OR we use a method called .rstrip("containing what we want to remove,so you put the character you want to remove in it")

#so
print("\n")
my_file = open("dna.txt")
my_dna = my_file.read().rstrip("\n")
dna_length = len(my_dna)
print("sequence is "+my_dna+" and length is "+str(dna_length))

#now what if we want to do stuff like write into the file what do we do we use a modifoed form of the open function which takes two arguements open(dna.txt,"w"or "a"or "r"),w writes stuff at the begining of the text in the file ,a appends or write dtuff at the end of the stuff in the file ,r which is the de4fault ,just allows us to read the file but instead of storing the file in a variable in when using read ,write behaves like the print function
print("\n")
my_file = open("out.txt","w")
my_file.write("Hello world without ghana ,im going crazy...i dunno")
# write "abcdef"
my_file.write("\nabc" + "def")
# write "8"
my_file.write('\n'+str(len('AGTGCTAG')))
# write "TTGC"
my_file.write("\nATGC".replace('A', 'T'))
# write "atgc"
my_file.write("\nATGC".lower())
# write contents of my_variable
my_variable = '\nomega alpha'
my_file.write(my_variable)