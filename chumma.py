from fuzzywuzzy import process

'''
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


'''
def hi(a,b):
    #print("fun")
    #print(type(b))
    dosa=b.split(" ")
    print(dosa)
    f=len(a)
    j=0
    vandhachu=0
    #print("length of names")
    #print(f)
    while(j<f):
        result=process.extract(a[j],dosa)
        #print(type(result))
        #print("for a[j]")
        print(a[j])
        print(result)
        oo=[y[0] for y in result]
        print(oo)
        g=[x[1] for x in result]
        print(g)
        leng=len(g)
        #print("lengthhhuh")
        #print(leng)
        j=j+1
        i=0
        while(i<leng):
            #print(g[i])
            #print("gof i")
            if(g[i]>=80):
                temp=oo[i]
                print(temp)
                #print(g[i])
                vandhachu=1
                break
            i=i+1
        if(vandhachu==1):
            return vandhachu
            break
        
    #print("done")
    

'''
a="srisharaan"
b="oh okk apdi check panalam paakalam reco aagudha nu srisharaan hi how are you im fine"
aa=re.match(a,b)
print(aa)
'''
#a=["elakkeya","elukeya","elackiya","elakiya"]
#b="can you please turn the mic on eluckya and keys"
#velila=hi(a,b)
#print(velila)
