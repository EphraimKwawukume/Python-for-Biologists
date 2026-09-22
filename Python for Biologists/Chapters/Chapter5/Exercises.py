def give_amino_acid_percent (proseq, a_code): #.upper() cannot be used in a function parameter definition. Parameters must be variable names
    proseq = proseq.upper()
    a_code = a_code.upper()
    proseq = proseq.replace('X','')
    length = len(proseq)
    amino_acid_count = proseq.count(a_code)
    amino_acid_percent = (amino_acid_count/length)*100
    return amino_acid_percent


assert give_amino_acid_percent("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert give_amino_acid_percent("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert give_amino_acid_percent("msrslllrfllfllllpplp", "L") == 50
assert give_amino_acid_percent("MSRSLLLRFLLFLLLLPPLP", "Y") == 0

print (give_amino_acid_percent ("MSRSLLLRFLLFLLLLPPLP", "M"))
print (give_amino_acid_percent ("MSRSLLLRFLLFLLLLPPLP", "L"))
print (give_amino_acid_percent ("MSRSLLLRFLLFLLLLPPLP", "r"))
print (give_amino_acid_percent ("MSRSLLLRFLLFLLLLPPLP", "Y"))

def give_amino_acid_percent1 (proseq, a_code = ['A', 'I', 'L', 'M', 'F', 'W', 'Y']): 
    proseq = proseq.replace('X','')
    length = len(proseq)
    total = 0
    for aa in a_code :
        amino_acid_count = proseq.count(aa)
        total = total + amino_acid_count
    amino_acid_percent = (total/length)*100
    return round(amino_acid_percent, 2)
                       
assert give_amino_acid_percent1 ("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert give_amino_acid_percent1 ("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert give_amino_acid_percent1 ("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert give_amino_acid_percent1 ("MSRSLLLRFLLFLLLLPPLP") == 65

print (give_amino_acid_percent1 ("MSRSLLLRFLLFLLLLPPLP", ["M"]))
print (give_amino_acid_percent1 ("MSRSLLLRFLLFLLLLPPLP", ["M", "L"]))
print (give_amino_acid_percent1 ("MSRSLLLRFLLFLLLLPPLP", ["F", "S", "L"]))
print (give_amino_acid_percent1 ("MSRSLLLRFLLFLLLLPPLP")) == 65

#i was seeing how the code would behave before placing it into the function
#protein = ("MSRSLLLRFLLFLLLLPPLP")
# aa_list = ['A', 'I', 'L', 'M', 'F', 'W', 'Y']
#aa_list = ['M', 'L']
#total = 0
#for aa  in aa_list :
#    aa_count = protein.count(aa)
#    total = total+aa_count
#    print("Amino Acid; " + ' ' + aa + ': ' + str(aa_count) + " so total at this point: " + str(total))

#length = len(protein)
#amino_acid_percent = (total)/length *100
#print (amino_acid_percent)


     






