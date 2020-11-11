
import re


def hello(a,b):

    
    #print("error")
    b=str(b)
    #print(b)
    #n=len(b)
    dosa=b.split()
    n=len(dosa)
    #print("size of the word")
    #print(n)
    #print("size of name")
    temp=len(a)
    #print(temp)
    i=0
    j=0
    boom=0
    o=0
    while(i<n):
        c=dosa[i]
        #print(c)
        f=len(c)
        #print("matching")
        while(o<f):
            if(a[j]==c[o]):
                j=j+1
                flag=j/f
                if(flag>0.5):
                    boom=1
                    #print(flag)
                    return boom
                    break
                
            else:
                j=0
            o=o+1
        i=i+1
    if(boom==0):
        return boom
def hi(a,b):
    t1=a
    t2=b
    bo=0
    z=str(a)
    #print(type(z))
    #print(z)
    x=str(b)
    #print(type(x))
    #print(x)
    pls=re.search(z,x)
    if pls:
        #print("regex")
        bo=1
        return bo
    else:
        #print("calling hi")
        hello(t1,t2)
