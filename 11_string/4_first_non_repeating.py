no_of_chars = 256

def get_count(string):
	count = [0] * no_of_chars
	for i in string:
		count[ord(i)] += 1
	return count

def first_non_repeating(string):
	count = get_count(string)
	index = -1
	k = 0

	for i in string:
		if count[ord(i)] == 1:
			index = k
			break

		k+=1

	return index


string = "geeksforgeeks"
index = first_non_repeating(string)
if (index == 1):
	print("All repeating or string empty")
else:
	print(string[index])