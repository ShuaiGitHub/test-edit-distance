
count = 0
fullTrainingResult=[]
fullTestResult=[]
oneTrainingResult=[]
with open('test.txt','r') as f:
	for line in f:
		cur_line = line.strip("\n")
		#because space is also used for alignment, so only the \n is removed.
		if cur_line.isdigit():
			oneTrainingResult.append(int(cur_line))
		elif cur_line.startswith("TRU"):
			oneTrainingResult.append(cur_line)
			assert (len(oneTrainingResult)==2)
		elif cur_line.startswith("OUT"):
			oneTrainingResult.append(cur_line)
			assert (len(oneTrainingResult)==3)
			fullTrainingResult.append(oneTrainingResult)
			oneTrainingResult=[]
		elif cur_line.startswith("ERROR"):
			cur_test_error = cur_line.split()
			assert (len(cur_test_error)==4)
			fullTestResult.append(cur_test_error)
		else:
			continue
		count = count + 1
print count