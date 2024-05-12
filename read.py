data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		count += 1
		data.append(line)
		if count % 1000 == 0:
			print(len(data))
print(len(data))

data_sum = 0
for d in data:
	data_sum += len(d)
data_ave = data_sum/len(data)
print(data_ave)	
