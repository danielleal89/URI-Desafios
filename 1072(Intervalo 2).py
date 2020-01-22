N = int(input())
count = 0
inn = 0
out = 0
while count < N:
    count = count + 1
    X = int(input())
    if X >= 10 and X <= 20:
        inn = inn + 1
    else:
        out = out + 1
print('{} in'.format(inn))
print('{} out'.format(out))