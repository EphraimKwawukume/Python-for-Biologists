# Processing DNA in a file
# A: 
with open('input.txt',) as file, open("cleaned.txt","w") as new_file:
    for line in file:
        #adapter = line[:14]
        #print(line.rstrip(adapter)) #was not working because the rstrip method treats its argument as a set of characters and removes those characters only from the right end, while your adapter is at the left.
        #print(line.replace(adapter,""),end="") #this works because the replace method replaces all occurrences of a substring with another substring, regardless of their position in the string. So it will remove the adapter from the left end of the line as well as any other occurrences of it in the line.and the end='' argument is used to prevent print() from adding an extra newline after each line, which would result in double spacing between lines.but there's an issue with this approach: if the adapter sequence appears elsewhere in the line (not just at the beginning), it will also be removed, which may not be what you want. If you only want to remove the adapter from the start of the line, you can use slicing instead:
        cleaned = line[14:]
        new_file.write(cleaned) #this doesnt have the print problem of adding a new line hence no ,end='' resulting into two spacing instead of the next sequence moving to the next line. The write() method writes the string to the file without adding any extra characters, so it preserves the original formatting of the line.
        print(cleaned.rstrip('\n') + ': ' + str(len(cleaned)) + '\n', end = '' ) #this will remove the first 14 characters from each line, which is the adapter sequence. The end='' argument is used to prevent print() from adding an extra newline after each line, which would result in double spacing between lines.OR i could use the lstrip() method to remove the adapter from the left end of the line, like this:
        #print(line.lstrip(adapter),end="") #this will remove the adapter sequence from the left end of each line, and the end='' argument is used to prevent print() from adding an extra newline after each line, which would result in double spacing between lines.OR i could also use print(line.removeprefix(adapter), end="")

print('\n')
#Multiple exons from genomic DNA

with open("genomic_dna.txt") as my_file, open("exons.txt") as pos:
    genomic_dna = my_file.read()
    coding_seq = ''
    for line in pos:
        positions = line.strip().split(',')
        start = int(positions[0])
        stop = int(positions[1])
        #print(positions, end='')
        exon= genomic_dna[start:stop]
        coding_seq = coding_seq + exon
    print('coding_seq= ' + coding_seq) #if print was in the for loop we would get prints for all th iterations for the loop i want the final hence put it out the loop
    with open ('coding_seq.txt,','w') as new_file:
        new_file.write(coding_seq)
    