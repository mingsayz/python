def reverse(text):
    return text[::-1]

def is_palindrome(text):
    list = []
    forbidden = ('.','?','!','-','/',',',' ')
    for i in text:
        if i not in forbidden:
            list.append(i.lower())

    return list == reverse(list)

something = input("Enter text:")
if is_palindrome(something):
    print('yes , it is a palindrome')
else :
    print('no, it is not a palindrome')
