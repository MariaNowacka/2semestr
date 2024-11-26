import string
import random
moja_lista=string.ascii_letters+string.digits+string.punctuation
def haslo(ile=8,jakie=moja_lista):
    '''funkcja generująca losowe hasła
        input : ile (int) - długość hasła, domyślnie 8 znaków
                jakie (list) - lisa znaków, z których program 
                zbuduje hasło, domyślnie litery, liczby i znaki specjalne'''
    h=""
    for i in range(ile):
        h+=random.choice(jakie)
    return h

print(haslo())