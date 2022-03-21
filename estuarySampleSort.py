import os
from glob import glob

directory = os.getcwd()
f = open("sounds.json", "w+")
f.write("[\n")
count = 0
globalCount = 0
sampleList = []

directoryList = glob(directory+"/*/", recursive = True)

for folder in directoryList:
	for file in glob(folder+"*"):
		y = file.replace(directory+"/","")
		sampleList.append(y)

print(sampleList)

for file in sampleList:

	head, sep, tail = file.partition('/')
	newBank = head


for file in sampleList:
	head, sep, tail = file.partition('/')
	if head != newBank:
		count = 0
		newBank = head

	else:
		count += 1
	if globalCount == 0:
		f.write('{"url":"'+file+'","type":"audio","bank":"'+head+'","n":'+str(count)+'}')	
	else:
		f.write(',\n{"url":"'+file+'","type":"audio","bank":"'+head+'","n":'+str(count)+'}')	
	globalCount= 1




f.write("\n]")

f.close()



