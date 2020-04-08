alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def removeCharFromAlphabet(param):
	for letter in alphabet:
		if(letter == param):
			alphabet.remove(letter)
			break

file = open("states.txt")
name = file.read().replace("\n", " ")
file.close()

print(name)

result = "".join(dict.fromkeys(name))
result = sorted(result)

for letter in result:
	removeCharFromAlphabet(letter)

print(result)
print(alphabet)
