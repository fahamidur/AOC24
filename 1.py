with open('1.txt', 'r') as file:
	lines = file.readlines()


list1 = []
list2 = []
total = 0
for line in lines:
	line = line.strip()
	if line:
		a,b = line.split()
		list1.append(int(a))
		list2.append(int(b))

list1.sort()
list2.sort()
for r , l in zip(list1,list2):
	total  += abs(r - l)

print(f"total number of distance: {total}")

from collections import Counter

frequency = Counter(list2)

similarity_score = 0

for i in list1:
	if i in frequency:
		similarity_score += i*frequency[i]

print(f"Total similary score {similarity_score}")