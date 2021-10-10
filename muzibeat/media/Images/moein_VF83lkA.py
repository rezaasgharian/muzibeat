print({(x,y)for x in range (1,11)for y in range(1,11)})
print('\n\n*'*30)

print({(a,b)for a in range (1,11)for b in range(1,11)if a%2==0})

name =['ali','reza','saeed','moein','maryam']
family=['asgharian','tabasi','alifar','asadi','alavi']
print(f'\n\n zip code sample = {list(zip(name,family))}')
users = [(n,m) for n in name for m in family]
print(f'\n\nthe name list = {users}')

newtext = []
ttext = []

text = input('encrypt text = ')

for i in text:
    # print(ord(i))
    ora = ord(i)+3
    # print(ora)
    ttext.append(ora)
# print(ttext)

for ch in ttext:
    pt = chr(ch)
    print(pt,end='')
    # newtext.append(pt)
print(newtext)




tezt = input('pt text : ')
for z in tezt:
    zp = ord(z)-3
    zc = chr(zp)
    print(zc,end='')

