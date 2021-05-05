import string, random

# Ask the user how many characters password must have
length = input('How many characters password must have (Default 128)? ')
length = 128 if length == '' else int(length)

# Generate the password
randoms = ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Print the password
print(f'Generated Password: {randoms}')