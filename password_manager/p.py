def Encryption(s):
    encstr=""
    for i in s:
        if(ord(i))>=33 and (ord(i)<=64):
            temp=(ord(i)+26)
            if temp>64:
                temp=temp%64+32
            encstr=encstr+chr(temp)
        elif(ord(i))>=65 and (ord(i)<=96):
            temp=(ord(i)+17)
            if temp>96:
                temp=temp%96+64        
            encstr=encstr+chr(temp)
        elif(ord(i))>=97 and (ord(i)<=122):
            temp=(ord(i)+11)
            if temp>122:
                temp=temp%122+96
            encstr=encstr+chr(temp)
        elif(ord(i))>=123 and (ord(i)<=126):
           temp=(ord(i)+3)
           if temp>126:
                temp=temp%126+122
           encstr=encstr+chr(temp)
        else:
               encstr=encstr+chr(ord(i))
    return encstr
def Decryption(s):
    p=Encryption(s)
    decstr=""
    for i in p:
        if(ord(i))>=33 and (ord(i)<=64):
            decstr=decstr+chr((ord(i)-26-33)%32+33)
        elif((ord(i))>=65) and (ord(i))<=96:
            decstr=decstr+chr((ord(i) -17-65) % 32 + 65)
        elif((ord(i))>=97) and (ord(i))<=122:
            decstr=decstr+chr((ord(i) - 11 - 97) % 26 + 97)
        elif(ord(i))>=123 and (ord(i)<=126):
           decstr=decstr+chr((ord(i)-3-123)%4+123)
        else:
            decstr= decstr+chr(ord(i))
    return decstr
print("Enter the string to Encrypt and decrypt : ")
s=input()
print("Enter the key(Eg: 21) : ")

print("Encrypted String : ",Encryption(s))
print("Decrypted String : ",Decryption(s))