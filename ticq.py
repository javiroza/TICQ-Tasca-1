# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:57:17 2020

@author: javir
"""
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

""" C.2 """
simbols = [key for key in alfabet]
alfabet = {simbol:format(simbols.index(simbol),'05b') for simbol in simbols}
p = 0.1
simbol_aleatori = random.choice(simbols)

def paritat(binari):
    """Returns the parity of a given binary number"""
    s = 0
    for i in str(binari):
        if i == "1":
            s += 1
    return 0 if s % 2 == 0 else 1

def flip(bit):
    """Returns a bit flipped with respect to the given one"""
    return "0" if str(bit) == "1" else "1"

def canal(missatge,p):
    """Returns a tuple with the original message and the one that has passed a noise filter"""
    missatge_prima = str(missatge)+str(paritat(missatge))
    v = list(missatge_prima)
    for digit in missatge:
        r = random.random()
        if r > 1-p:
            v[v.index(digit)] = flip(digit)
            
    return (missatge_prima,"".join(v))

(missatge_original,missatge_filtrat)=canal(alfabet[simbol_aleatori],p)
print("APARTAT 2")
print("Missatge 1: "+missatge_original)
print("Missatge 2: "+missatge_filtrat+"\n")

# Càlcul de B.3
k = 50000
p = 0.01

def calculb3(p,k):
    """Returns the probability of a message being altered"""
    p_incorrecte = 0
    for i in range(0,k):
        (m1,m2)=canal(alfabet[random.choice(simbols)],p)
        if m1[:5] != m2[:5]:
            p_incorrecte += 1
    return p_incorrecte/k

print("P(incorrecte),p="+str(p)+": "+str(calculb3(p,k)))

# Càlcul de B.4
k = 50000
p = 0.1
def faildetected(m1,m2):
    """Returns True or False"""
    return True if paritat(m2[:5]) != int(m2[5]) else False

def calculb4(p,k):
    n_detectats = 0
    n_erronis = 0
    
    for i in range(0,k):
        (m1,m2)=canal(alfabet[random.choice(simbols)],p)
        if m1[:5] != m2[:5]: 
            n_detectats += 1 if faildetected(m1,m2) else 0
            n_erronis += 1 
        
    return 100*float(n_detectats)/float(n_erronis)

print("Es detecten els errors en un: "+str(format(float(calculb4(p,k)),'.2f')+"%"))