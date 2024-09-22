def is_palindrome(string):
    string = str(string)
    if not isinstance(string, str):
        return False
    clean_string = ''.join(char.lower() for char in string if char.isalnum())
    return clean_string == clean_string[::-1]

print(is_palindrome("A man, a plan, a canal -- Panama"))
print(is_palindrome("Madam, I'm Adam!"))
print(is_palindrome(333))
print(is_palindrome(None))
print(is_palindrome("Abracadabra"))













