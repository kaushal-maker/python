def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

examples = ["madam", "race car", "level", "noon", "A man a plan a canal Panama"]

for word in examples:
    if is_palindrome(word):
        print(f'"{word}" is a palindrome.')
    else:
        print(f'"{word}" is not a palindrome.')

# def is_palindrome(t):
#     t = t.replace(" ","").lower ()
#     return t == t[::-1]

# name = ['BoBt']

# for word in name:
#     if is_palindrome(word):
#         print(f'"{word}"yes')
#     else:
#         print(f'"{word}" na bro')