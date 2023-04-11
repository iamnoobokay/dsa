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
print(max(lst))
print(min(lst))
print(sum(lst))
print(all(lst))

filtered = list(filter((lambda x:x<3),lst))
# print(filtered)

words = str.split('The longest word in this sentence')
sor = sorted(words, key=len)
# print(sor)

dict1 = {'five':5,'four':4,'three':3,'two':2,'one':1,'zero':0}
# print(len(dict1))
# dict2 = dict1.copy()
# print(dict2)
# print(dict1.items())
# print(dict1.keys())
# print(dict1.pop('three'))
# print(dict1)
# print(sorted(list(dict1),reverse=True))
# print(sorted(list(dict1.values())))
# dict1.clear()
# print(dict1)


set1 = {'pranav','abc',1,2,3,4,('asd')}
set2 = {'poudyal','abc',6,7,8,5,4,('asd')}
set3 = {'zxc'}
set4 = {'pranav'}

print(set1-set2)
print(set2-set1)
print(len(set2))
print(set1.intersection(set2))
print(set2.intersection(set1))
print(set2.isdisjoint(set3))
print(set4.issubset(set1))
print(set1.issuperset(set4))
print(set1.symmetric_difference(set2))
print(set1.union(set2))