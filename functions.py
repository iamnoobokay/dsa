def greeting(language):
    if language == 'eng':
        return 'hello world'
    if language == 'fr':
        return 'Bonjour le monde'
    if language == 'pt':
        return 'ola mundo'
    else:
        return 'language not supported'
    

l = [greeting('fr'),greeting('pt')]
print(l)

def callf(f):
    lang = 'fr'
    return (f(lang))

print(callf(greeting))


lst = [1,2,3,4]
mapped = list(map(lambda x:x**3,lst))
print(mapped)

filtered = list(filter((lambda x:x<3),lst))
print(filtered)

words = str.split('The longest word in this sentence')
sor = sorted(words, key=len)
print(sor)