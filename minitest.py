# -*- coding: utf-8 -*-

# ------------
# Funktion
# ------------
def insert_AB(text):
    new_text = ''
    j = 0
    for i in range(len(text)):
        new_text += text[i]
        if j == 0 and i < len(text)-1:
            new_text += 'A'
            j = 1
        elif j == 1 and i < len(text)-1:
            new_text += 'B'
            j = 0
        else:
            pass
    return new_text


# ------------
# Testfälle
# ------------
print('------------ Testfälle ---------------')

print(insert_AB(''))
print(insert_AB('x'))
print(insert_AB('xx'))
print(insert_AB('xxxx'))
print(insert_AB('x' * 9))
