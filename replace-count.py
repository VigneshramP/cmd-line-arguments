import sys
def fileopen(fileOpen):
	f = open (fileOpen,"r")
	fileopen=(f.read())
	return fileopen 	
def replace_vowels(File,dictionary):
	LowerConversion = File.lower()
	for oldCharacter,newCharacter in dictionary.items():
		LowerConversion = LowerConversion.replace(oldCharacter,newCharacter)
	return LowerConversion
def count_of_character(File,dictionary):
	list_of_replaceCharacter = dictionary.values()
	for characterCount in list_of_replaceCharacter:
		print "The Count of {} is :".format(characterCount),File.count(characterCount)
def main():
	fileOpen = sys.argv[1]
	document = fileopen(fileOpen)
	dictConversion= dict([Character.split('-') for Character in sys.argv[2:]])
	replaceDocument = replace_vowels(document,dictConversion)
	count_of_replace_Characters = count_of_character(replaceDocument,dictConversion)
if __name__ == '__main__':
	main()