def translate(text):
    words = text.split()
    translated_words = []

    for word in words:
        translated_words.append(translate_word(word))
    return ' '.join(translated_words)

def translate_word(text):
    vowels = list('aeiou')
    if text[0] in vowels or text[:2] == 'xr' or text[:2] == 'yt':
        return add_ay(text)
    count = 0
    while text[0] not in vowels:
        if text[:2] == 'qu':
            text = move_first_letter_to_end(text)
            text = move_first_letter_to_end(text)
            break    
        if text[0] == 'y' and count > 0:
            break
        else:
            text = move_first_letter_to_end(text)
            count += 1
    return add_ay(text)

def add_ay(text):
    return text+'ay'
    
def move_first_letter_to_end(text):
    return text[1:]+text[0]