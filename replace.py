import sys
def fileopen(fileOpen):
	f = open (fileOpen,"r")
	fileopen=(f.read())
	return fileopen 	
def replace_vowels(File,dictionary):
	Lower = File.lower()
	for oldCharacter,newCharacter in dictionary.items():
		Lower = Lower.replace(oldCharacter,newCharacter)
	print "The Replacing File is :",Lower

def main():
	fileOpen = sys.argv[1]
	document = fileopen(fileOpen)
	dictConversion= dict([Character.split('-') for Character in sys.argv[2:]])
	replace_vowels(document,dictConversion)
if __name__ == '__main__':
	main()
