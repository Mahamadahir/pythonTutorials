def convert(number):
    sounds = {
        3 : "Pling",
        5 : "Plang",
        7 : "Plong"
    }
    correct_sound = ''
    for key, value in sounds.items():
        if number % key == 0:
            correct_sound += value
    return correct_sound or str(number)

        
