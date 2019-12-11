import hashlib
import pickle
def md5(a):
    temp=hashlib.md5(a.encode())
    x=temp.hexdigest()
    f=open('md5.bin','rb')
    paas=pickle.load(f)
    paas[a]=x
    f.close()
    f1=open('md5.bin','wb')
    pickle.dump(paas,f1)
    f1.close()
    return x

def sha1(a):
    temp=hashlib.sha1(a.encode())
    x=temp.hexdigest()
    f=open('sha1.bin','rb')
    paas=pickle.load(f)
    paas[a]=x
    f.close()
    f1=open('sha1.bin','wb')
    pickle.dump(paas,f1)
    f1.close()
    return x

def sha224(a):
    temp=hashlib.sha224(a.encode())
    x=temp.hexdigest()
    f=open('sha224.bin','rb')
    paas=pickle.load(f)
    paas[a]=x
    f.close()
    f1=open('sha224.bin','wb')
    pickle.dump(paas,f1)
    f1.close()
    return x

def sha256(a):
    temp=hashlib.sha256(a.encode())
    x=temp.hexdigest()
    f=open('sha256.bin','rb')
    paas=pickle.load(f)
    paas[a]=x
    f.close()
    f1=open('sha256.bin','wb')
    pickle.dump(paas,f1)
    f1.close()
    return x

def sha384(a):
    temp=hashlib.sha384(a.encode())
    x=temp.hexdigest()
    f=open('sha384.bin','rb')
    paas=pickle.load(f)
    paas[a]=x
    f.close()
    f1=open('sha384.bin','wb')
    pickle.dump(paas,f1)
    f1.close()
    return x

def sha512(a):
    temp=hashlib.sha512(a.encode())
    x=temp.hexdigest()
    f=open('sha512.bin','rb')
    paas=pickle.load(f)
    paas[a]=x
    f.close()
    f1=open('sha512.bin','wb')
    pickle.dump(paas,f1)
    f1.close()
    return x

def decrypt(b):
    f=open(b,'rb')
    lis=pickle.load(f)
    for j in lis:
        if lis[j]==e:
            print('Match Found: ',j)
            break
    else:
        print('No match found')
    
    f.close()
    
while True:
    t=int(input('What would you like to do? \n1)To hash \n2)To crack hash\nAny other number to quit\n'))
    if t==1:
        print('Select the type of hashing:\n')
        print('1)md5\n2)sha1\n3)sha224\n4)sha256\n5)sha384\n6)sha512\nAny other number to quit\n')
        i=int(input('Enter corresponding number: '))
        shash=input('Enter the string to be hashed:')
        if i==1:
            print(md5(shash))
        elif i==2:
            print(sha1(shash))
        elif i==3:
            print(sha224(shash))
        elif i==4:
            print(sha256(shash))
        elif i==5:
            print(sha384(shash))
        elif i==6:
            print(sha512(shash))
        else:
            break
    elif t==2:
        print('Select the type of hashing:\n')
        print('1)md5\n2)sha1\n3)sha224\n4)sha256\n5)sha384\n6)sha512\nAny other number to quit\n')
        i=int(input('What type of encryption would you like to crack?'))
        e=input('Please enter hash: ')
        if i==1:
            decrypt('md5.bin')
        elif i==2:
            decrypt('sha1.bin')
        elif i==3:
            decrypt('sha224.bin')
        elif i==4:
            decrypt('sha256.bin')
        elif i==5:
            decrypt('sha384.bin')
        elif i==6:
            decrypt('sha512.bin')
        else:
            break
    else:
        break
                


    
    
    