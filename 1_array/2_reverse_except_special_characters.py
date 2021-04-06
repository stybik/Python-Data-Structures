def reverse(string):
	LIST = list(string)
	r = len(LIST) - 1
	l = 0

	while(l < r):
		if not LIST[l].isalpha():
			l += 1
		elif not LIST[r].isalpha():
			r -= 1

		else:
			LIST[l], LIST[r] = LIST[l], LIST[r]
			l += 1
			r -= 1

	return ''.join(LIST)

string = "a!!!b.c.d,e'f,ghi"
print("Input string: " + string)
string = reverse(string) 
print("Output string: " + string)