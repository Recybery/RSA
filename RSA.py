import math
import sys
import Pow
#central functions
def encrypt(M,bs,e,n):
    f=make(str(M),3)
    i=0
    batches=split(f,bs)[0]
    tail=split(f,bs)[1]
    while i<len(batches):
        batches[i]=str(Pow.resMod(int(batches[i]),e,n))
        i+=1 
    return [batches, tail]
def dencrypt(M,bs,d,n):
    a=[]
    c=""
    i=0
    end=len(M[0])
    while i<end:
        if(i!=end-1):
            c=make(str(Pow.resMod(int(M[0][i]),d,n)),bs)
        else:
            c=make(str(Pow.resMod(int(M[0][i]),d,n)),M[1])
        a.append(c)
        i+=1
    return a
#importanat math
def gcd(a,b):
    if(a%b==0):return b
    else: return gcd(b,a%b) #euclidean algorithm
def findInverse(k,d):
    return findHelp(k,d,0,1)%k
def findHelp(k,d,m1,m2):
    q=k/d#more euclidean algorithm 
    r=k%d#
    m3=m1-q*m2
    if(r==1):
        return m3
    return findHelp(d,r,m2,m3)    
def findCoprime(K): 
    n=findCoHelp(K,K,Pow.pow(10,100,10))
    while(gcd(n,K)!=1 or n==0):
        n-=1
    return n
def findCoHelp(K,k,d):
    try:
        a=int(math.floor(math.sqrt(k)))
        b=gcd(a,K)
        return a
    except OverflowError, err:
        a=k/d
    return findCoHelp(K,a,d)
def prod(b):
    N=1
    K=1
    for s in b:
        N*=s
        K*=(s-1)
    return [N,K]
#data management
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
def batchToString(M):
    a=""
    end=len(M)
    i=0
    while i<end:
        a+=M[i]
        i+=1
    return a
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


def main(message):
    source=[ 47636001527157843615510166362212813825553995166349359052560828063795751982743949356281378571281356684995526346349689115319412565735006540850254022130876377867983398374239198108049044484863543699346022227692817853215225730056764957039852693911896900286014520659611654434776741074401112976951,
        203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790123]
    N=prod(source)[0]
    K=prod(source)[1]
    bs=len(str(N))-1
    d=findCoprime(K)
    E=findInverse(K,d)
    print "d= "+str(d)
    print "e= "+str(E)
    print "gcd(k,d)= "+ str(gcd(K,d))
    print "d*e mod K = "+str((d*E)%K)
    startM=message
    #("A+/109Z ;lskdjf;lakdjfl;aa;lkjfa;lsjfa;lsdkjfal;sdkjfff;alsdkfjasl;kdfjasl;kjfa;sldkjfla;sdkjfasl;kdjfal;skdjflskdjflaskdjfla;skdjfalskdjfla;skdjfla;skdjoquwenbg;oishb3po4i5u;o97foiahq3;o8a'uu ;qo8w4ysisdygv9a8tyeg'qkuahsfl9ua[8=aq32]qg\r q]3\408kjfdl;aksjdfl;ka!!!!!sjdzzzzzzzzzzzzzzzzzzfl;aksjdfl;askjdfa               ")
    B=encode(startM)
    print "B:"+make(str(B),3)
    print "decoded(B):"+str(decode(B)) 
    Coded=encrypt(B,bs,E,N)
    print "number of batches =  "+str(len(Coded[0]))
    Bp=dencrypt(Coded,bs,d,N)
    print "encrypted:"+batchToString(Coded[0])
    endM=decode(batchToString(Bp))
    print "message:"+endM
    if endM==startM:
        print "the message was successfully encrypted and decrypted"
    else:
        print "fuck. god damnit. shit"

    #'''
try:
    main(sys.argv[1])
except IndexError, err:
   # print " give it an argument you silly goose"
   main("you know you can use the command line to input a message. right? "
       # ''' comment this line to  make the message shorter
      +"Also Your mother was a hampster and your father smelt of eldeberries"
   #"djhdkhgdkhgfjgfhgdg"
    # asdf   +"a;s[]pe9iru0[i4n4'iono4oihjwo;lrig0e9oerter-=-w=-e=-1=1=-1=-1=2-1=-2=1-][s-]d-bc]-ep;lwirj'l;ksj;fkdahj//z/// // / // / / /safig'hjaihelskdjfa;lskdfj;alskdjf;laskdjf;alskdjf;laskdjf;alsk"
     # wwwwwwww  +j"as;lkdfj;alskdjf;alskdjf;lakhpoq[uwireh[oadcvih[0984yuh;oli34hy0s8d9fby0[384h;oiwyuq230q384yhiouyafd08[gyh3q[o4ihr0q[3284h[0sdi8fhb[083h43[08h[dosifhg0-834h[oiswerhh"
   #+"gggggggggggggggggggggggggggggggggggggggggdurjgdsddddddddddddddddddddddddddddddddddddddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeutrweuyeiyeiytritdiktdikutdkutdkutdkutdkutdkytdkutydkytdktudkutkttktkttktktt"
   #'''
    )