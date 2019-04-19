# This programm will show you how strong your password is
# If your password is weak, program will generate new and strong password.
# Just write your password

import re, password_generator

password = input(str('Enter your password: '))

#good password is if it has minimum 8 signs, inculde small and big letters and has minimum one number
#strong password is if it has minimum 8 signs, inculde small and big letters, minimum one number and one special sign e.g. exclamation mark (!)

good_password = re.compile(r'''
^(?=.*[A-Z])
(?=.*[a-z])
(?=.*\d)
(.{8,})$
''', re.VERBOSE)

strong_password = re.compile(r'''
^(?=.*[A-Z])
(?=.*[a-z])
(?=.*\d)
(?=.*[(){}[@/|:;<>+^$!%*?&'`~])
(.{8,})$
''', re.VERBOSE)
print(strong_password.findall(password))
if len(strong_password.findall(password)) == 1 :
    print('Your password: '+ str(''.join(strong_password.findall(password))) + " is strong password. You don't need to change it.")
elif len(good_password.findall(password)) == 1:
    print('Your password: '+ str(''.join(good_password.findall(password))) + " is good password. You can change it but you dont need to do it.")
    password_generator.new_password_question()
else:
    print('Your password: ' + password + " is too weak ! Change it as fast as it is possible !")
    password_generator.new_password_question()

