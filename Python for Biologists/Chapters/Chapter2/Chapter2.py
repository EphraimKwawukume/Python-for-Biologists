print("hello world")
print("fuck this shit") 
print ("gwrgwer")
print("'hello world'")
print("\"hello world\"")
#backwards slash before both quatoation marks 
print("Name\nDate")
#the \n allows us to push the Date to the next line,otherwis if we did it this way we would get an error ("Name
#Date ") we would get an error ,the compiler would think Date is a new code and we are making a mistake 
#the compiler reads line by line ,so it expects a string statement to have an end quatoation marks and a parenthesis otherwise it would think its an error

#concatenation
banku = "AGTA"
hand='PUNANI'
print(banku)
print(hand)
oreo='GCT' +' '+ hand
print(oreo)
yam=hand +' '+banku
print(yam+' '+'CAT')
#this thing ive been doing is known as concatenation ,you can join strings and fuctions together in the definition of a string or even in the print argument
ink="AGATCG"
sizeink=len(ink)#find lenght of a string
print("LENGHT OF INK IS " + str(sizeink))
#WE CANT CONCATENATE STRINGS TO INT SO WE USE STR TO CONVERT THE INT TO A STRING 
#str is a function which takes one argument (whose type is number), and returns a value (whose type is string) representing that number.
#BUT YOU CAN DO THIS THOUGH
print("66 is the same as " + "sixty six")#the reason why sizeink had to converted to a string format was because it was stored as an INT

#using a method
my_dna="AGTAA"
print(my_dna.lower())
print(my_dna)
print(len(my_dna))
my_newdna="agagcccttt"
print(my_newdna.upper())
#upper and lower are what you call method and method work for only a type it won't work on an INT only a STRING

#REPLACEMENT
protein="ytqednnml"
#replace tyrosine with alanine
print(protein.replace("y","a"))
#or replace ytq with qih
print(protein.replace("ytq",("qih")))
#nothing changes in the stored value of protein only the printed versions
#lets see if i can chnage words not in sequence like qdl with vvy
print(protein.replace("qdl","vvy"))#no you can't
print(protein)#to show that the protein does not change
#lemme see if can store the replacement
new_protein=protein.replace("y","b")
print(new_protein)#yhup you can 

#extracting a part out of a string called taking a subtring,we indicate the start and end positions ,positions start at 0
MY_WORDS="IMAGINE THERE WAS NO HEAVEN NO HELL BELLOW"#I WANT PRINT OUT ONLY THE NO HEAVEN TO THE END PART,SO IT STARTS AT 18 AND THE END POINT YOU DONT NEED TO NECCESSARILY TYPE THE EXACT NUMBER IF YPUR USING IT TO THE END ,JUST WRITE ANY RANDOM LARGE NUMBER,IMMA DO TWO WHERE THE SECOND IT WILL END AT HELL HENCE THE END POINT WILL BE 34,damn actually it was 35,34 prints HEL this is because the positions are inclusive at the start, but exclusive at the stop. In other words, the expression MY_WORDS[18:35] gives us everything starting at the 18TH character (N), and stopping just before the 35TH character (WHICH IS A SPACE)THE34TH CHARACTER WAS  
print(MY_WORDS[18:1111])
print(MY_WORDS[18:35]) 
#OR YOU CAN USE LEN FUNCTION TO KNOW THE TOTAL LENGTH OF YOUR STRING
print(len(MY_WORDS))
print(MY_WORDS[18:42])

#counting the number or times a word or letter repeated itself in a string
protein_b="nevwvyvygnvtiyvavyagg"
valine_count=protein_b.count('v')
vy_count=protein_b.count('vy')
glycine_count=protein_b.count('g')
print("valine count: " + str(valine_count))
#because the valine count is stored as an int i used str
print("vy count: " + str(vy_count))
print("glycine count: " + str(glycine_count))
#now if you want to find the location of a residue in the sequence we use a find 
print(protein_b.find('v'))
#this ha s limitation because there are several instancesof v ,n=but the print out will be 3 for only the first v ,showing location of only one v and not the others
print(protein_b.find('vy')+ protein_b.find('g'))
#print(protein_b.find('vy')+ protein_b.find('g')) will print ou 12 that is 4 + 8 thewy will add to prevent that i use str
print(str(protein_b.find('vy'))+' '+ str(protein_b.find('g')))

print("dfvjdsvjsdcvfffffffffffffffffffffffffffffffff")