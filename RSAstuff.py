import math
base64_String="ABCDEFGHIJKLNMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"#veryImportant string
def gcd(a,b):
    if(a%b==0):return b
    else: return gcd(b,a%b)
def resPowMod(B,e,n):
    return resPowMod2(B,e,n,10)
def resPowMod2(B,e,n,P): 
    B=B%n
    if e<0: return int( resPowMod2(1.0/B,-e,n,P))
    if e==0:return 1
    elif e==1:return B
    if e<P:
        return resPo(B,e,n)
    i=e%P
    return resPo(B,i,n)*resPowMod2(resPo(B,P,n),(e-i)/P,n,P)%n
def resPo(B,e,n):
    B=B%n
    if e<0: return resPo(1.0/B,-e,n)
    if e==0:return 1
    elif e==1:return B
    elif e%2==0:return resPo(B*B,e/2,n)
    elif e%2==1:return B*resPo(B*B,(e-1)/2,n)
def encrypt(M,bs,e,n):
    f=make(str(M),3)
    i=0
    batches=split(f,bs)[0]
    tail=split(f,bs)[1]
    while i<len(batches):
        batches[i]=str(resPowMod(int(batches[i]),e,n))
        i+=1 
    return [batches, tail]
def split(M,bs):
    batches=[]
    i=0
    j=-1
    end=len(M)#+(f if f!=bs else 0)
    while i<end:
        if(i%bs==0):
            j+=1
            batches.append("")
        try:
            batches[j]+=M[i]
        except Exception:
            pass
        i+=1     
    tail=len(batches[j])
    return [batches, tail]
def dencrypt(M,bs,d,n):
    a=[]
    c=""
    i=0
    end=len(M[0])
    while i<end:
        if(i!=end-1):
            c=make(str(resPowMod(int(M[0][i]),d,n)),bs)
        else:
            c=make(str(resPowMod(int(M[0][i]),d,n)),M[1])
        a.append(c)
        i+=1
    return a
def batchToString(M):
    a=""
    end=len(M)
    i=0
    while i<end:
        a+=M[i]
        i+=1
    return a
def findInverse(k,d):
    return findHelp(k,d,0,1)%k
def findHelp(k,d,m1,m2):
    q=k/d
    r=k%d
    m3=m1-q*m2
    if(r==1):
        return m3
    return findHelp(d,r,m2,m3)    
def make3(s):
    if(len(s)%3==1):
        s="00"+s
    elif(len(s)%3==2):
        s="0"+s
    return s
def make(s,n):
    while(len(s)%n!=0):
        s="0"+s
    return s
def encode(s):
    out=""
    for ch in s:
        out+=make3(str(ord(ch)))
    return int(out)
def decode(s):
    l=str(s)
    l=make3(l)
    #print l
    out=""
    i=0
    while i< len(l):
        a=chr(
              int(l[i]+l[i+1]+ l[i+2] )
              )
        i+=3
        out+=a
    return out
def prod(b):
    N=1
    K=1
    for s in b:
        N*=s
        K*=(s-1)
    return [N,K]
def enBase64(inpu):
    
    output=""
    binString=""
    try:
        for ch in inpu :
            binString+=format(ord(ch),"08b")
        batches=split(binString,6)
        for i in batches[0]:
            output+=base64_String[int(i,2)]
        if batches[1]==2:
            output+= "="
        if batches[1]==4:
            output+="=="
        return output
    except TypeError, e:
        return enBase64(str(bin(inpu)).split('b')[1])
def toBin(L):
    s=""
    try:
        while L>0:
            s+=str(L%2)
            L=L/2
        return s
    except Exception,e :
        pass# write for when L eis string of a decimal number         
def index64(ch):
    for i in range(0,len (base64_String)):
        if ch==base64_String[i]:
            return i    
    return None

def deBase64Bin(l):
    a=str(l)
    binString=""
    for ch in a:
        if(ch!='='):
            
            binString+=str(format(index64(ch),'08b'))   
            print binString   
        else:
            pass
    return binString
def deBase64(l):
    binString=deBase64Bin(l)
    output=""
    batches=split(binString,8)
    for i in batches[0]:
        output+=str(int(i,2))
    return int(output)
source=[ 47636001527157843615510166362212813825553995166349359052560828063795751982743949356281378571281356684995526346349689115319412565735006540850254022130876377867983398374239198108049044484863543699346022227692817853215225730056764957039852693911896900286014520659611654434776741074401112976951,
        203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790123]
#source=[7,23]
N=prod(source)[0]
K=prod(source)[1]
bs=len(str(N))-1
print "first!"
print str(format(12,'08b'))
L=  ("mQINBFUhMwMBEACyJicQKBIJZuQ5dmCufAipViOEWTYuIJczHC9N2AMZYAA5/wKpNTX4K9/j"
+"NS/it6UbMtFnJD0c8/JpyBNvh7kIaBUe1DHE/4g8oPsRQd+SEWdYDxd/kWt3gtfFGwusnhSo"
+"8V+qtBfcffoCCuMN3zmMiIT5FKKRK59YEfk/WRCbrL9WZncXu8uaj5peKxknVS7ceYc6tbhg"
+"D5gzme8DYBnP0jZp+SimYTocuA9ptQPbwk9JIRG8ZRWynGyeUB7y5m5kU2PMkHGinuF/8R9O"
+"xyuzRXewVZrwrM+aGyPE8HRaPlSs+ly1+l7G1meuSrKq2yVbHakETjH1SwrZLcu/ks5NXhVg"
+"O91HmO0AUMil6QOqSyh7MvMPn0FIft4hMJ64oUfMhPXOF+mTaMb+vfOp4wuS9YfBh2iCsLA8"
+"xdgUqRXRmei4MJ9VTwHSXOnXNRQrFMHn/dNgh8Ni6BZDaLhrHDX+AShPAvMl07Z7jCxg3OpG"
+"gVpssAcxmhw06r7kb8rYdj4oMLyvxyTuj/HBKs+4/o9wvsParpe2evy+rmgb1fP8UZuRqrui"
+"xUJVfufePHwxB+QtxmJtJj3Zpvfubfl3th1QBYremZ8Mye163fVWs92kXjwFlloO+7BoMJ+G"
+"k+coNB6QAHMF1DnkHCVvSTaAaGFXQ/QkUh/Nvg3vvRkghOxwkwARAQABtCpOaWNrIEVjb25v"
+"cG91bHkgPG5pY2tlY29ub3BvdWx5QGdtYWlsLmNvbT6JARwEEAEKAAYFAlUhO7wACgkQ0Jfx++=")
#''''

print L
PP=deBase64Bin(L)
print PP
print "up"
print index64('B')
d=int(math.floor(math.sqrt(K/1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
      #resPowMod(2,len(str(K)),len(str(K)))
      ) ) )
print gcd(K,d)
while gcd(K,d)!=1: 
    d-=1

startM=("A+/109Z ;lskdjf;lakdjfl;askjfdl;aksjdfl;ka!!!!!sjdzzzzzzzzzzzzzzzzzzfl;aksjdfl;askjdfa               ")
B=encode(startM)
print "B:"+make(str(B),3)
print "decode(B):"+str(decode(B))

Coded=0
E=findInverse(K,d)
#othere=findInverses(d,K)
print "d:"+str(d),
print "  e:"+str(E)
#print "othere:"+str(othere)
print "check Inverse:"+str((d*E)%K)
f=split(make3(str(B)),bs)[0]
Coded=encrypt(B,bs,E,N)
Bp=dencrypt(Coded,bs,d,N)
print "encrypted:"+batchToString(Coded[0])
endM=decode(batchToString(Bp))
print "message:"+endM
print endM==startM
#'''