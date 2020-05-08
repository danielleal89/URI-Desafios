C = int(input())
for i in range(C):
    p = input()
    print('{:.2f}'.format(int((p.count('') - 1)) / 100))