import argparse
def ArgParser():
  parser=argparse.ArgumentParser(description = "Replacing Character in Sting")
  parser.add_argument("-f","--file",help = "File path use -f")
  parser.add_argument("-s","--Character",help="Format EXAMPLE:a-b-c-d and use -s")
  args=parser.parse_args()
  return args
def fileOpen(file):
  f=open(file,"r")
  fileOpen= f.read()
  return fileOpen
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
  Args= ArgParser()
  fileContant=fileOpen(Args.file)
  Replace=Args.Character.split("-")
  dictConversion = {Replace[i]: Replace[i + 1] for i in range(0, len(Replace),2)} 
  LowerConversion=replace_vowels(fileContant,dictConversion)
  Count_of_character = count_of_character(LowerConversion,dictConversion)

if __name__ == '__main__':
  main()
