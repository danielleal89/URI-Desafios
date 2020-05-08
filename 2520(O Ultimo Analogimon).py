# -*- encoding: utf-8 -*-
um = []
dois = []

while True:
    try:
        n = list(map(int, input().split(' ')))
        for i in range(n[0]):
            a = list(map(int, input().split(' ')))
            for j, item in enumerate(a):
                if item == 1:
                    um.append(i+1)
                    um.append(j+1)
                elif item == 2:
                    dois.append(i+1)
                    dois.append(j+1)

        c1 = um[0] - dois[0] if um[0] > dois[0] else dois[0] - um[0]
        c2 = um[1] - dois[1] if um[1] > dois[1] else dois[1] - um[1]
        print(c1 + c2)
        um.clear()
        dois.clear()

    except:
        break