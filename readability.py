from cs50 import get_string

# Prompt user for text

while True:
    text = get_string("Text: ")
    break

# Count number of letters in text

letters = 0
for i in text:
    if i.isupper() == True:
        letters += 1
    elif i.islower() == True:
        letters += 1

# Count number of words in text

words = text.count(' ') + 1

# Count number of sentences in text

sentences = text.count('.') + text.count('!') + text.count('?')

# Calculate number of letters per 100 words

averageLetters = float((float(letters) / float(words)) * 100)

# Calculate number of sentences per 100 words

averageSentences = float((float(sentences) / float(words)) * 100)

# Calculate Coleman-Liau

colemanLiau = float(0.0588 * float(averageLetters) - 0.296 * float(averageSentences) - 15.8)

# Print final results

if colemanLiau < 1:
    print("Before Grade 1\n", end="")
elif colemanLiau > 16:
    print("Grade 16+\n", end="")
else:
    print("Grade " + str(round(colemanLiau)))
