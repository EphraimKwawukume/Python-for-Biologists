file1 = open('data.csv')
for line in file1:
    org = line.rstrip('\n').split(',')
    species_name = org[0]
    sequence = org[1]
    gene_name = org[2]
    expression_level = org[3]
    if species_name == "Drosophila melanogaster" or species_name == 'Drosophila simulans':
        print(species_name + ': ' + gene_name)
file1.close()
print('\n')
file1 = open('data.csv')
for line in file1:
    org = line.rstrip('\n').split(',')
    species_name = org[0]
    sequence = org[1]
    gene_name = org[2]
    expression_level = org[3]
    if len(sequence) >= 90 and not len(sequence) > 110:
        print(species_name + ': ' + gene_name)
file1.close()
print('\n')
def at_rich(dna):
    length = len(dna)
    A_count = dna.upper().count('A')
    T_count = dna.upper().count('T')
    AT_content = (A_count + T_count)/length
    return AT_content
file1 = open('data.csv')
for line in file1:
    org = line.rstrip('\n').split(',')
    species_name = org[0]
    sequence = org[1]
    gene_name = org[2]
    expression_level = org[3]
    if at_rich(sequence) < 0.5 and float(expression_level) > 200: #split(',') returns strings, so expression_level is a string.hence needs to be converted to a number before
        print(species_name + ': ' + gene_name)
file1.close()
print('\n')
file1 = open('data.csv')
for line in file1:
    org = line.rstrip('\n').split(',')
    species_name = org[0]
    sequence = org[1]
    gene_name = org[2]
    expression_level = org[3]
    if (gene_name.startswith('k') or gene_name.startswith('h')) and species_name != 'Drosophila melanogaster': #we could have also used and not species_name == 
        print(species_name + ': ' + gene_name)

print('\n')
file1 = open('data.csv')
for line in file1:
    org = line.rstrip('\n').split(',')
    species_name = org[0]
    sequence = org[1]
    gene_name = org[2]
    expression_level = org[3]
    if at_rich(sequence) > 0.65:
        print(species_name + ': ' + gene_name + " AT content is High")
    elif at_rich(sequence) < 0.45: 
        print(species_name + ': ' + gene_name + " AT content is Low")
    else:
        print(species_name + ': ' + gene_name + " AT content is Medium")