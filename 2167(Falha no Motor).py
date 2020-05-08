n = int(input())
v = input().split()
for i in range(1, len(v)):
    if int(v[i]) < int(v[i-1]):
        print(i+1)
        exit()
print('0')