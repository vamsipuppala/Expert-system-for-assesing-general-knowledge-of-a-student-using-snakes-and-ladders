import random
l=[]
def ranq():
    return random.randrange(0,39,2)
def question(opt):
    f = open('my_text_file.txt', "r")
    lines = f.readlines()
    if(len(l)==20):
        l.clear()
    p=1
    while(p==1):
        vals=ranq()
        if(vals not in l):
            l.append(vals)
            break
    print(lines[vals])
    f.close()
    x=input()
    if(lines[vals+1].lower()==(x+"\n").lower()):
        return True
    else:
        if(opt==1):
            print("the correct answer is... ")
            print(lines[vals+1])
        return False


    #print(lines1[c-1])
    #print(x)
    #print(x)
    #print(lines1[c-1])
