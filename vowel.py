# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count

# # Example
# text = "Hello, World!"
# print("Number of vowels:", count_vowels(text))










# def count_vowel(s):
#     vowel = 'aeiouAeiou'
#     count = 0

#     for char in s:
#         if char in vowel:
#             count+= 1
#     return count


# example = "kaushal"
# print("no. of vowels are",count_vowel(example))










def count_vowel(c):
    vowel= "AEIOUaeiou"
    count = 0

    for char in c:
        if char in vowel:
            count+= 1

    return count

example = "Kaushal Kishore Pathak"

print("ye le",count_vowel(example))