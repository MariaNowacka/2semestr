import string
import random
moja_lista=string.ascii_letters+string.digits+string.punctuation
def haslo(ile=8,jakie=moja_lista):
    h=""
    for i in range(ile):
        h+=random.choice(jakie)
    return h

print(haslo())
