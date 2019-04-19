import pyperclip, random, string, sys

def generate(
char1 = string.ascii_letters,
char2 = string.digits,
char3 = string.ascii_lowercase,
char4 = string.ascii_uppercase,
char5 = string.punctuation):
    global new_password
    new_password = ''.join(random.choice(char1)+random.choice(char2)+random.choice(char3)+random.choice(char4)+random.choice(char5) for _ in range(2))
    pyperclip.copy(new_password)
    print('Your new password is: ' + new_password + ". Now this password is in your clipboard.")

def new_password_question():
    question = input(str('Do you want to generate new, random, strong password ? (Y/N): '))
    if question == "Y" or question == "y":
        generate()
        save_to_file()
    else:
        sys.exit(0)

def save_to_file():
    save = input('Do you want to save it to the file ? (Y/N): ')
    if save == 'Y' or save == 'y':
        safe_password = open('safe_password.txt', 'w')
        safe_password.write(new_password)
        safe_password.close()
    else:
        sys.exit()
