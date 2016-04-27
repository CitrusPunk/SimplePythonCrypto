import sys

if (__name__ == "__main__"):
		
	def readFile (path):
		file = open(path, "r")
		lineList = []
		for line in file:
			lineList.append(line)
		#print(lineList)
		return lineList

	def encrypt (lines,x):
		encrypted = []
		for line in lines:
			for idx in range(0,len(line)-1):
				num = ord(line[idx])+x
				while(num < 0):
					num += 256
				while(num > 255):
					num -= 256
				char = chr(num)
				encrypted.append(char)
			encrypted.append("\n")
		return encrypted

	def writeFile(path, encrypted):
		file = open(path, "w")
		for char in encrypted:
			file.write(char) #print(char)
		file.close

	if(len(sys.argv) < 4):
		print("INPUT ERROR")
		print("try:\npython caesar.py \"number\" \"path\" \"-e\\-d\"") 
	else:
		num = int(sys.argv[1])
		path = sys.argv[2]
		crypt = sys.argv[3]
		lines = readFile(path)

		if(crypt == "-d"):
			num = num * (-1)
			encrypted = encrypt(lines, num)
		elif(crypt == "-e"):
			encrypted = encrypt(lines, num)
		writeFile(path, encrypted)
