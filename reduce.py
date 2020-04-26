file1 = open("bookfilter.txt") 
line = file1.read()# Use this to read file content as a stream: 
#line = line.decode("utf-8")
words = line.split() 
mymap = dict()
for r in words:
	if r in mymap.keys():
		mymap[r] += 1
	else:
		mymap[r] = 1
appendFile = open('wordcounter.txt','w')
appendFile.write(str(mymap))
appendFile.close() 
print("Task Complete")