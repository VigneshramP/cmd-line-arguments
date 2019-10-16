import sys
def fileopen(fileOpen):
	f = open (fileOpen,"r")
	fileopen=(f.read())
	return fileopen 	
def replace_vowels(File,dictionary):
	Lower = File.lower()
	for oldCharacter,newCharacter in dictionary.items():
		Lower = Lower.replace(oldCharacter,newCharacter)
	print Lower
def dictionaryConvert(List): 
    Split_Dict = {List[i]: List[i + 1] for i in range(0, len(List),2)} 
    return Split_Dict 
def main():
	fileOpen = sys.argv[1]
	document = fileopen(fileOpen)
	replacingCharacters = sys.argv[2:]
	split = []
	for Split in replacingCharacters:
		split.append(Split.split("-"))
	print split
	listConversion = []
	for i in split:
		for j in i:
			listConversion.append(j)
	print listConversion
	dictConversion = dictionaryConvert(listConversion)
	print dictConversion
	replace_vowels(document,dictConversion)
if __name__ == '__main__':
	main()