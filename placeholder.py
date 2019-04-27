
library_1 = [
    "A",
    "a",
    "the",
    'of',
    "as",
    "with",
    "is",
    "and",
    "to",
    "when",
    "will",
    "make",
    "in",
    "or",
    "if",
    'it', 'helpful', 'to', 'read', 'your', 'work', 'aloud.', 'when', 'you', 'you', 'make', 'end', 'or', 'if', 'there', 'no', 'in', 'your', 'writing,', 'you', 'can', 'be', 'almost', 'certain', 'that', 'you', 'have', 'written', 'run-on', 'sentence.'
]

def seperation(string_input):
    # string_input = string_input.split(" ")
    for word in string_input:
        if word in library_1:
            string_input.remove(word)
    print(string_input)

def sample(word):
    print(len(word))


if __name__ == '__main__':
    first_text = input("Enter a sentence > ")
    # caseignore = first_text.casefold()
    # listed = caseignore.split(" ")
    # seperation(listed)
    sample(first_text)

# remove !@#$%^&*()":><{?{>
# remove a the of with
