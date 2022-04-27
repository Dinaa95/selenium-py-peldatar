# Írj programot, mely addig olvas be számokat a billentyűzetről, ameddig azok kisebbek, mint tíz.
# Írja ki ezek után a beolvasott számok összegét!

x = int(input('Give a number: '))
total = 0
while x < 10:
    y = int(input('Gimme moreeee: '))
    total += y
    if y < 10:
        continue
    else:
        break
print(x + total)
