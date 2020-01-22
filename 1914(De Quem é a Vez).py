testes = int(input())
for i in range(testes):
    pri, esc_pri, seg, esc_seg = input().split()
    num_pri, num_seg = input().split()
    p = [pri, esc_pri, num_pri]
    s = [seg, esc_seg, num_seg]
    calc = int(num_pri) + int(num_seg)
    if calc % 2 == 0:
        if esc_pri == 'PAR':
            print(pri)
        else:
            print(seg)
    else:
        if esc_pri == 'IMPAR':
            print(pri)
        else:
            print(seg)
