def get_at_content(dna, sig_figures=2):
    dna = dna.replace('N','')
    length = len(dna)
    a_count = dna.count('A')  
    t_count = dna.count('T')
    at_content =(a_count + t_count)/length
    return round(at_content, sig_figures)
    
#Firstly, we need to make a clear distinction between defining a function, and running it (we refer to running a function as calling it).  The code we've written above will not cause anything to happen when we run it, because we've not actuallyasked Python to execute the get_at_content function – we have simply defined what it is
#The code in the function will not be executed until we call the function like this:
get_at_content("AGTACCATTGCGTAACGTGCA") #If we simply call the function like that, however, then the AT content will vanish once it's been calculated. In order to use the function to do something useful, we must either store the result in a variable or use itdirectly in print
at_content = get_at_content("AGTACCAGGGGGGTTGCGTAACGTGCA")
print(str(at_content))
#OR
print(str(get_at_content("AGTACCATTGCGTAACGTGCA")))

#Secondly, it's important to understand that the argument variable dna does not hold any particular value when the function is defined1. Instead, its job is to hold whatever value is given as the argument when the function is called. In this way it'sanalogous to the loop variables we saw in the previous chapter: loop variables hold a different value each time round the loop, and function argument variables hold a different value each time the function is called.
#also just like the arguments in a loop any variables that we create as part of the function only exist inside the function, and cannot be accessed outside
#for example; 
# print(a_count) #we get an error becauese we have not define a_count, a_Count was only defined in the function, which has been locked off
my_at_content = get_at_content('ATGCGCGATTTAGGTTTTTTTACGATCGAATCG')
print(str(my_at_content)) #print(str(my_at_content, 3)) we cant do this because of str and 3 is int: unless we do 
content = 'ATGCGCGATTTAGGACTTGATCGAATCG'
print(get_at_content(content,5))
print(str(get_at_content("ATGCATGCAACTGTAGC",4))) #prior to adding the round function to the get_at_content function the output was a number which significant figures of 10,we want to reduce it 2 ,using return round (the int variable,the significant figure we want),but what if we want to be able to decide the number of sig figures in print ,because its not always we want up to 2 sig figures,so now when we try to call the function we have to add the significant figures we want
print(str(get_at_content('atgacgtagtacccgttagg'))) #output is zero becaue not same as capital

#Function dont always need to have an argument
#Occasionally you may be tempted to write a no-argument function that works like this:
def get_at_content1(): 
    length = len(dna) 
    a_count = dna.upper().count('A') 
    t_count = dna.upper().count('T') 
    at_content = (a_count + t_count) / length 
    return round(at_content, 2) 

dna = "ACTGATCGATCG" #so that anywhere you write in your code its linked to the function but
print(get_at_content1())
# At first this seems like a good idea – it works because the function gets the value of the dna variable that is set on line 35.  However, this breaks the encapsulation(independency- allowing us to break up large code into bits so they dont become too large or dependent on us and other code:also allowing us to work bit by bit) that we worked so hard to achieve. The function now only works if there is a variable called dna set in the bit of the code where the function is called, so the two pieces of code are no longer independent. If you find yourself writing code like this, it's usually a good idea to identify which variables from outside the function are being used inside it, and turn them into arguments.
print('\n')
#Functions don't always have to return a value
def get_at_content2(dna):
    length = len(dna)
    a_count = dna.count("A")
    t_count = dna.count('T')
    at_content = (a_count + t_count)/length
    print(round(at_content,2))

get_at_content2('AGACATACAGTGCGCGCCGATAGCGCG') #OUTPUT; 0.37
#When you first start writing functions, it's very tempting to do this kind of thing. You think "OK, I need to calculate and print the AT content – I'll write a function that does both". The trouble with this approach is that it results in a function that is less flexible. Right now you want to print the AT content to the screen, but what if you later discover that you want to write it to a file, or use it as part of some other calculation? You'll have to write more functions to carry out these tasks. The key to designing flexible functions is to recognize that the job calculate and print the AT content is actually two separate jobs – calculating the AT content, and printing it. Try to write your functions in such a way that they just do one job. You can then easily write code to carry out more complicated jobs by using your simple functions as building blocks.

print('\n')
#Functions can be called with named arguments
# What do we need to know about a function in order to be able to use it? We need to know what the return value and type is, and we need to know the number and type of the arguments. For the examples we've seen so far in this book, we also need to know the order of the arguments. For instance, to use the open function we need to know that the name of the file comes first, followed by the mode of the file. And to use our two-argument version of get_at_content as described above, we needto know that the DNA sequence comes first, followed by the number of significant figures. There's a feature in Python called keyword arguments which allows us to call functions in a slightly different way. Instead of giving a list of arguments in parentheses:
#we can also call fuctions like this
print(get_at_content(dna = "AGAGATCTCCCCCTTTAGAGATCTCT", sig_figures = 4))  #with the named variables and when we write it this way we can write it in any order 
print(get_at_content( sig_figures = 4, dna = "AGAGATCTCTAGATTAGAGATCTCT"))
#It works with methods too, including all the ones we've seen so far.

#Function arguments can have defaults
#if you look at get_at_content (dna,sig_figures =2) we have function whose default is 2, similar to how the open function has a default mode of read

#Testing functions
# we compare the the answer given by the called function the a known answer for example
#  For example, we know that if we run our get_at_content function on the DNA sequence "ATGC" we should get an answer of 0.5. This assertion will test whether that's the case:
assert get_at_content ('ATGC') == 0.5 #if its correct nothing will show if its wrong we will get an Assertion Error
#If we get some unexpected output from a program that uses a particular function, and the assertion tests for that function all pass, then we can be confident that the error doesn't lie in the function but in the code that calls it. 
#Also helps us know that after modifying a function we haven't introduced any Errors
#Assertions are also useful as a form of documentation
#vFinally, we can use assertions to test the behaviour of our function for unusual inputs.Say will happen if the sequencehas a series of unknown bases N hwo ewill our function work
assert get_at_content ("ATGCNNNNNNNNNNN") == 0.5
 # WE GET AN ASSERTION ERROR DUE TO OUR FUNCTION ADDING THE N-UNKOWN BASES SO WHAT WE IS TO FIX FOR THE N PROBLEM  IN OUR FUNCTION ## now we get no issues
#It's common to group a collection of assertions for a particular function together to test for the correct behaviour on different types of input
assert get_at_content ("A") == 1
assert get_at_content ('G') == 0
assert get_at_content ('ATGC') == 0.5
assert get_at_content ("AGG") == 0.33
assert get_at_content("AGG", 1) == 0.3
assert get_at_content("AGG", 5) == 0.33333
