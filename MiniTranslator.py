# Vowels
# if we see vowel letter ( aeiou ) in phrase
# aeiou -> g
# change it into g
'''
Not Printing out -- This is for block of comments
'''
def translate(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate((input("Enter a phrase: "))))


def minitranslate(phrase):
    translation=""
    for letter in phrase:
       if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
       else:
           translation = translation + letter
    return translation

print(minitranslate((input("Enter a phrase: "))))