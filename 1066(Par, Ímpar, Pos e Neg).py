a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
pos = 0
neg = 0
par = 0
imp = 0

if a > 0 and a != 0: pos = pos + 1
if a < 0 and a != 0: neg = neg + 1
if b > 0 and b != 0: pos = pos + 1
if b < 0 and b != 0: neg = neg + 1
if c > 0 and c != 0: pos = pos + 1
if c < 0 and c != 0: neg = neg + 1
if d > 0 and d != 0: pos = pos + 1
if d < 0 and d != 0: neg = neg + 1
if e > 0 and e != 0: pos = pos + 1
if e < 0 and e != 0: neg = neg + 1

if a%2 == 0: par = par + 1
else: imp = imp + 1
if b%2 == 0: par = par + 1
else: imp = imp + 1
if c%2 == 0: par = par + 1
else: imp = imp + 1
if d%2 == 0: par = par + 1
else: imp = imp + 1
if e%2 == 0: par = par + 1
else: imp = imp + 1

print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(imp))
print('{} valor(es) positivo(s)'.format(pos))
print('{} valor(es) negativo(s)'.format(neg))