# -*- encoding: utf-8 -*-
n = int(input())
dic = {'saque':0, 'bloqueio':0, 'ataque':0, 'saqueA':0, 'bloqueioA':0, 'ataqueA':0}

for i in range(n):
    nome = input()
    tentativa = list(map(int, input().split(' ')))
    acerto = list(map(int, input().split(' ')))
    dic['saque'] += tentativa[0]
    dic['bloqueio'] += tentativa[1]
    dic['ataque'] += tentativa[2]
    dic['saqueA'] += acerto[0]
    dic['bloqueioA'] += acerto[1]
    dic['ataqueA'] += acerto[2]

print('Pontos de Saque: {:.2f} %.'.format((dic['saqueA'] / dic['saque']) * 100))
print('Pontos de Bloqueio: {:.2f} %.'.format((dic['bloqueioA'] / dic['bloqueio']) * 100))
print('Pontos de Ataque: {:.2f} %.'.format((dic['ataqueA'] / dic['ataque']) * 100))