#!/usr/bin/python3.5
class Item:
	def __init__(self):
		self._name = " "
		self._parentdir = " "
class File(Item):
	def __init__(self):
		self._size = 0
class Directory(Item):
	def __init__(self):
		self._Update = 0
		self.filesInDir = []
	def addFile(self,File):
		self.filesInDir.append(File)
	def printFiles(self):
		for myfile in self.filesInDir:
			print("  ",myfile.name)		

def printMenu():
	print(" ")
	print("Main Menu")
	print("1.Create a File")
	print("2.Create a Directory")
	print("3.Remove a File/Directory")
	print("4.Display File System")
	print("5.Exit") 

def deleteDir(choiceDir):
	for myDir in rootdir:
		if myDir.name == choiceDir:
			rootdir.remove(myDir)
			print("Directory successfully deleted")
			return True
	print("directory: <",choiceDir,"> not found")
	return False

def deleteFile(choiceFile):
	for myDir in rootdir:
		for myfile in myDir.filesInDir:
			if myfile.name == choiceFile:
				myDir.filesInDir.remove(myfile)
				print("File successfully deleted")
				return True
	print("file: <",choiceFile,"> not found")
	return False

def sortAll():
	sortedRootdir = {}
	for myDir in rootdir:
		sortedRootdir = {myDir.name : myDir}
	
		

x = 0 
rootdir = []
while x != '5':
	printMenu()
	print("")
	x = input("Enter your choice: ")
	if x == '1':
		myfile = File()
		inputname = input("Please enter a File name or quit: ")
		inputparentdir = input("Please enter a parent directory or quit: ")
		myfile.name = inputname
		for myDir in rootdir:
			if myDir.name == inputparentdir:
				myfile._parentdir = inputparentdir
				myDir.addFile(myfile)
				print("Created file:",myDir.name,"/",myfile.name)					
	if x == '2':
		dirName = input("Enter directory name: ")
		myDir = Directory()
		myDir.name = dirName
		print(myDir.name)
		rootdir.append(myDir)
	if x == '3':
		fileOrDir = input("Delete a FILE or DIRECTORY? (F/D): ")
		if fileOrDir == "D":	
			choiceDir = input("Enter a directory to delete: ")
			deleteDir(choiceDir)
		elif fileOrDir == "F":
			choiceFile = input("Enter a file to delete: ")
			deleteFile(choiceFile)
				
		
	if x == '4':
		sortAll()
		for myDir in rootdir:
			print(myDir.name)
			myDir.printFiles()
	if x !='1' and x !='2' and x !='3' and x !='4' and x !='5':
		print("ERROR: Try again: ")
print("Goodbye!")	
		
