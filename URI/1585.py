# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
ordem = int(raw_input())
for i in xrange(ordem):
    a,b = [int(i) for i in raw_input().split(" ")]
    print "%s cm2" % str(a*b/2)
