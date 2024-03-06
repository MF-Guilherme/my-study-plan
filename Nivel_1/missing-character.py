def missing_chars(word):
    missing = []
    alfabeth = 'abcdefghijklmnopqrstuvwxyz'
    word_lowwercase = word.lower().replace(' ','')
    
    for letter in alfabeth:
        if not letter in word_lowwercase:
            missing.append(letter)
    if missing:
        missing_concat = ''.join(missing)
        return missing_concat
    else:
        return('The string is a pangram.')

input = input()

print(missing_chars(input))