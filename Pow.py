import math
def biPow(B,e):
    if e<0: return int (biPow(1.0/B,-e))
    if e==0:return 1
    elif e==1:return B
    elif e==2:return B*B
    return biPow(B,e%2)*biPow(B*B,e/2)
def resMod(B,e,n):
    return resModH(B,e,n,5)
def resModH(B,e,n,P): 
    B=B%n
    if e<0: return int( resModH(1.0/B,-e,n,P))
    if e==0:return 1
    elif e==1:return B
    if e<P:
        return biPow(B,e)
    i=e%P
    return biPow(B,i)*resModH(biPow(B,P),(e-i)/P,n,P)%n
def pow(B,e,P):
    if e<0: return int( pow(1.0/B,-e,P))
    if e==0:return 1
    elif e==1:return B
    if e<P:
        return pow(B,e,P)
    i=e%P
    return pow(B,i,P)*pow(biPow(B,P),(e-i)/P,P)
