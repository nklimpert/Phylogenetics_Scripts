import os

data = {}

num = ''
with open(fasta, 'r') as inFile:
	for line in inFile:
		if line.startswith('>'): #if it's a header line
			num = line.split('_')[-1].strip()
			if num not in data:
				data[num] = [line]
			else:
				data[num].append(line)
		else: #if it's a bait line
			
