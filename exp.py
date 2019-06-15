s1=0
s2=0
def ert(p):
    global s1
    s1+=1
    if(p==1):
        global s2
        s2+=1
    return s1,s2    
