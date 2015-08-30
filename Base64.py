base64_String="ABCDEFGHIJKLNMOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"#veryImportant string
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
    except Exception, errora:
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
            binString+=format(index64(ch),'08b')   
    return binString
def deBase64(l):
    binString=deBase64Bin(l)
    output=""
    batches=split(binString,8)
    for i in batches[0]:
        output+=str(int(i,2))
    return int(output)
