from userInterface import *

def main():
    var=1
    while(var==1):
        print("enter regdno :")
        regd=int(input())
        print("enter name")
        name=input()
        print("enter section name")
        sec=int(input())
        if(regd>100000000 and regd<999999999 and sec>0 and sec <23):
            break
        else:
            print("invalid input")
    for i in range(10):
        master = Tk()
        master.title("Snake and Ladder")
        master.geometry("850x600")
        img = PhotoImage( file = "lenna.gif")
        x = Display(master,img,regd,name,sec)
        master.mainloop()

main()
