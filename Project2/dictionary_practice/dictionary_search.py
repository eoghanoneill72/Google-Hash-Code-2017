
def load_text(filename):
    with open(filename, "r") as f:
        text = f.read()
    text_clean = text.split(' ')
    return text_clean

# Load some text into an array
text = load_text('corpus.txt')

# Adding elements to dictionary - Remember, there cannot be duplicate keys

# Declare empty dictionary
dictionary = dict()
for word in text:
    # Check if the word is in the dictionary already, if not, create new key. If it is, add to it's value.
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1

# Get all keys from dictionary
words = dictionary.keys()

# Get all values from the dictionary
word_counts = dictionary.values()

# Print the frequency of the word 'the'
print('Word count for "the":', dictionary.get('the'))

# Rank by frequency
# Convert into a data structure that will gauranntee that the order of the elements will be maintained.
to_array = []
# Note how we iterate through the key AND the corresponding value
for k, v in dictionary.items():
    to_array.append((k,v))

def sorted_dict_alt(array):
    # Look familiar? bubble sort! (Slightly modified), you can use any sorting algorithm
    for i in range(len(to_array)):
        for current in range(len(to_array)-1):
            if array[current][1] < array[current+1][1]:
                temp = to_array[current]
                array[current] = array[current+1]
                array[current+1]= temp
    return array


# The easy way? Use the sorted method with an anonymous function (dreaded lambda) which returns the key for each item.
sorted_dict= sorted(dictionary.items(), key = lambda x : x[1])

# Print ranked words
print(sorted_dict_alt(to_array))