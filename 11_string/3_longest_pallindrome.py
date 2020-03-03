def get_longest_pallindrome(str):
	n = len(str)
	ans = []

	for l in range(n, 0, -1):
		found = False
		for s in range(n-l+1):
			target = str[s:s+l]
			if target == target[::-1]:
				ans.append(str[s:s+l])
				found = True

		if found:
			break

	return ans if str else ['']

print(get_longest_pallindrome("abcaaaczsh"))