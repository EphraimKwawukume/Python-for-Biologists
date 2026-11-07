import sys

# sys.argv[0] is the script name ('counter.py')
# sys.argv[1] is the sequence text
# sys.argv[2] is the letter we want to count

sequence = sys.argv[1]
letter = sys.argv[2]

# Count occurrences
count = sequence.count(letter)
cent = (count/len(sequence))*100

print(f"Analyzing: {sequence}")
print(f"Total count of '{sequence}': {len(sequence)}")
print(f"Total count of '{letter}': {count}")
print(f"Percentage of '{letter}': {cent}" +' %')