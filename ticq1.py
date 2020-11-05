# -*- coding: utf-8 -*-
# Progamat amb Python (versió 3)

import random

""" C.1 """
alfabet = {"-":0.17,"E":0.13,"A":0.12,"I":0.07,"S":0.06,"O":0.06,"R":0.05,"L":0.05,"N":0.05,"T":0.04,"U":0.04,"D":0.03,"C":0.03,"M":0.02,"P":0.02,"V":0.01,"Q":0.01,"B":0.009,"G":0.009,"F":0.007,"H":0.005,"X":0.003,"Y":0.003,"J":0.002,"Ç":0.001,"Z":0.0005,"K":0.0003,"W":0.0002}
huffman_alfabet = {"-":"100","E":"110","A":"010","I":"1010","S":"1110","O":"0110","R":"0000","L":"0001","N":"0010","T":"10111","U":"10110","D":"11110","C":"01110","M":"00111","P":"00110","V":"011110","Q":"111110","B":"111111","G":"111110","F":"0111110","H":"11111110","X":"01111111","Y":"11111110","J":"111111110","Ç":"1111111110","Z":"11111111110","K":"111111111110","W":"111111111111"}

simbols = list()
m = 200000

def decide(r):
    """Returns a random symbol of dictionary 'alfabet'"""
    s = 0
    for value in alfabet:
        s += alfabet[value]
        if r <= s :
            return value

def generador(m):
    """Returns a list with m random symbols from dictionary 'alfabet'"""
    l = 0
    for i in range(0,m):
        r = random.random()
        simbol = decide(r)
        simbols.append(simbol)
        l += len(huffman_alfabet[simbol])
        
    long_mitjana = l/m
    return (simbols,long_mitjana)

(llista,lmitj) = generador(m)
print("APARTAT 1")
print("Longitud mitjana calculada sobre "+str(m)+" símbols: "+str(lmitj)+"\n")

