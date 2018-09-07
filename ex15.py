#
from sys import argv
#
script, filename = argv
prompt = '-----> '

txt = open (filename)

#
print(f'Here is your file {filename}:')
print (txt.read())
print("type that file name again:")
file_again = input("> ")
txt_again = open(file_again)

print (txt_again.read())
