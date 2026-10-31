import re
#Quantifiers, let us describe variation in the number of times a section of a pattern is repeated.
# ? A question mark following a character means that that character is optional – it can match either zero or one times.
# GAT?C the T is optional, and the pattern will match either GATC or GAC. If we want to apply a question mark to more than one character, we can group the characters in parentheses. For example, in the pattern GGG(AAA)?TTT the group of three As is optional, so the pattern will match either GGGAAATTT or GGGTTT.
# + A plus sign following a character or group means that the character or group must be present but can be repeated any number of times - it will match one or more times.
# For example, the pattern GGGA+TTT will match
# GGGATTT, GGGAATT, GGGAAATT, etc. but not GGGTTT.
# * An asterisk following a character or group means that the character orgroup is optional, but can also be repeated. In other words, it will match zero or more times. 
# For example, the pattern GGGA*TTT will match GGGTTT, GGGATTT, GGGAATTT, etc. 
# If we want to specify a specific number of repeats, we can use curly brackets. Following a character or group with a single number inside curly brackets will match exactly that number of repeats. For example, the pattern GA{5}T will match GAAAAAT but not GAAAAT or GAAAAAAT. Following a character or group with a pair of numbers inside curly brackets separated with a comma allows us to specify an acceptable range of number of repeats. For example, the pattern GA{2,4}T will match GAAT, GAAAT and GAAAAT but not GAT or GAAAAAT. 

# Positions
# ^  The caret symbol matches the start of a string when not in a character group ^ if in a character group [^] signifies negation, and 
# $  The dollar symbol matches the end of a string. 
#The pattern ^AAA will match AAATTT but not GGGAAATTT. 
#The pattern GGG$ will match AAAGGG but not AAAGGGCCC.

#^ATG[ATGC]{30,1000}A{5,10}$ 
# an ATG start codon at the beginning of the sequence
# followed by between 30 and 1000 bases which can be A, T, G or C
# followed by a poly-A tail of between 5 and 10 bases at the end of the sequence
# = ATGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAAA 

# or it can mean

# ATGAAAAAAAAAAAAATTTTAAAGGGGGGGGGGGGAAAAAAAAAAAGGGGG AAAAA 

#Positions
dna = 'ATGACGTACGTACGACTG'
#storing the match object in a variable m
m = re.search(r'GA([ATGC]{3})AC',dna)
print(m.group()) #output; GACGTAC

m = re.search(r'GA([ATGC]{3})AC([ATGC]{2})AC',dna)
#re.search(r'GA*[ATGC]{3}*AC*[ATGC]{2}*AC',dna) will give you an index error if you dont put the groups in paranthesis...put the bracket where i have put the *
print('entire match: ' + m.group())
print('first match: ' + m.group(1)) #first match: CGT
print('second match: ' + m.group(2)) #second match: GT

#Getting the position of a match
#The start and end methods get the positions of the start and end of the pattern on the sequence
m = re.search(r'GA([ATGC]{3})AC([ATGC]{2})AC',dna)
print('start: ' + str(m.start())) #output: 2. ..remember we start from index 0 so G=0,A=1,c=2 which is the start 
print("end: " + str(m.end()))
#We can get the start and end positions of individual groups by supplying a number as the argument to start and end
m = re.search(r'GA([ATGC]{3})AC([ATGC]{2})AC',dna)
print('start: ' + str(m.start()))
print("end: " + str(m.end()))
print('group 1 start: ' + str(m.start(1)))
print('group 1 end: ' + str(m.end(1)))
print('group 2 start: ' + str(m.start(2)))
print('group 2 end: ' + str(m.end(2)))

#Splitting a string using a regular expression
#split a string using a regular expression pattern as the delimiter. The normal string split method doesn't allow this, but the re module has a split function of its own that takes a regular expression pattern as an argument. The first argument is the pattern, the second ar
#So imagine we have a consesus DNA sequence that contains ambiguity codes, and wewant to extract all runs of contiguous unambiguous bases. We need to split the DNA string wherever we see a base that isn't A, T, G or C:
dna = 'ACTNGCATRGCTACGTYACGATSCGAWTCG'
runs = re.split(r'[^ATGC]',dna) #caret ^ at the start of a character group negates it...so im saying split at anywhere you dont see a ATGC
# PS [^...] = NOT (negation)   ^... = Starts with (position anchor)
print(runs) #Output: ['ACT', 'GCAT', 'GCTACGT', 'ACGAT', 'CGA', 'TCG']

#Finding multiple matches
#The examples we've seen so far deal with cases where we're only interested in a single occurrence of a pattern in a string. If instead we want to find every place where a pattern occurs in a string, there are two functions in the re module to help us. 
# re.findall returns a list of all matches of a pattern in a string.
# Say we want to find all runs of A and T in a DNA sequence longer than five bases
dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
runs = re.findall(r'[AT]{4,100}',dna)
print(runs)#Output: ['ATTATAT', 'AAATTATA']
#the return value of the findall method is not a match object – it is a straightforward list of strings so we have no way to extract the positions
#If we want to do anything more complicated than simply extracting the text of the matches, we need to use the 
#re.finditer method. finditer returns a sequence of match objects, so to do anything useful with it, we need to use the return value in a loop
dna = "ACTGCATTATATCGTACGAAATTATACGCGCG"
runs = re.finditer(r"[AT]{3,100}", dna)
for section in runs:
    run_start = section.start()
    run_end = section.end()
    print('AT rich region from: ' + str(run_start) + ' to ' + str(run_end)) #Output: AT rich region from: 5 to 12 AT rich region from: 18 to 26
#finditer gives us considerably more flexibility that findall.
#the pattern GG(A|T)CC to describe the AvaII restriction enzyme recognition site, but it could also be written as 
#• GG[AT]CC,
#• (GGACC|GGTCC) 
#• (GGA|GGT)CC
#• G{2}[AT]C{2}
#As with other situations where there are multiple different ways to write the same thing, it's best to be guided by what is clearest to read. 
