from collections import Counter

test_cases = int(input())
test_count = 0
tweet_names = []

for i in range(test_cases):
	num = int(input())
	for j in range(num):
		name = str(input())
		tweet_names.append(name)


unique_names = [names.split()[0] for names in tweet_names]
times = Counter(unique_names)

repeat = times.values()

for element in set(repeat):
	dupl = ([(key, value) for key, value in sorted(times.items()) if value == element])

	if len(dupl) > 1:
		for (key, value) in dupl:
			print (key,'',value)

	max_value = max(times.values())
	temp_max_result = [(key, value) for key, value in sorted(times.items()) if value == max_value]

	if temp_max_result != dupl:
		for (key,value) in temp_max_result:
			print (key,'',value)