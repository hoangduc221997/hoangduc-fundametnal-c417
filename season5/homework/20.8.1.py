data = input("Enter your data:").lower()
letter_counts={}
for letter in data:
    letter_counts[letter]=letter_counts.get(letter, 0) + 1
letter_items = list(letter_counts.items())
letter_items.sort()
for value in letter_items:
    print(*value,end="\n")
