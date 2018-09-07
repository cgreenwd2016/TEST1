#
from sys import argv
#
script, user_name = argv
prompt = '---------> '

print ()
print('hi {user_name}, I am the {script} script.')
print ('I would like to ask you a few questions')
print ('do you like me {user_name} ?')
#
likes = input (prompt)
print ('where do you live {user_name}')
lives = input (prompt)
print ('what kind of computer do you have?' )
computer = input(prompt)

print (f"""
alright you said {likes} about me
you live in {lives}. Not sure where where that is.
and you have a {computer} computer. Nice.
""")
