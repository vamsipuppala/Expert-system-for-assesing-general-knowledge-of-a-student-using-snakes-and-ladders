from exp import *
import random
from tkinter import *
from diceMove import dice
import time
from quest import question
def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle

class MatchPosition():
    def find_snake_or_ladder(self, block, turn, position,tyu):
        #print(tyu)
        x = 35*(turn>=3)
        y = (turn%3)*35
        if(block == 3):
           if((turn==0 and question(tyu)==True) or turn==1):
               if(turn!=1):
                   print("right answer!!!")
                   print("you can climb the ladder")
               if(turn==1):
                   print("computer climbed the ladder")
               return 305+x, 150+y, 22
           else:
               print("wrong answer!!!")
               print("you can't climb the ladder")

               return position[0], position[1], block
        elif(block == 5):
            if((turn==0 and question(tyu)==True) or turn==1):
                if(turn!=1):
                    print("right answer!!!")
                    print("you can climb the ladder")
                if(turn==1):
                    print("computer climbed the ladder")
                return 545+x, 390+y, 8
            else:
                print("wrong answer!!!")
                print("you can't climb the ladder")
                return position[0], position[1], block
        elif(block == 11):
            if((turn==0 and question(tyu)==True) or turn==1):
                if(turn!=1):
                    print("right answer!!!")
                    print("you can climb the ladder")
                if(turn==1):
                    print("computer climbed the ladder")
                return 185+x, 30+y, 26
            else:
                print("wrong answer!!!")
                print("you can't climb the ladder")
                return position[0], position[1], block
        elif(block == 20):
            if((turn==0 and question(tyu)==True) or turn==1):
                if(turn!=1):
                    print("right answer!!!")
                    print("you can climb the ladder")
                if(turn==1):
                    print("computer climbed the ladder")
                return 545+x, 30+y, 29
            else:
                print("wrong answer!!!")
                print("you can't climb the ladder")
                return position[0], position[1], block
        elif(block == 17):
            if((turn==0 and question(tyu)==False) or turn==1):
                if(turn!=1):
                    print("wrong answer!!!")
                    print("you couldnt escape from the snake")
                if(turn==1):
                    print("computer bit by snake")

                return 425+x, 510+y, 4
            else:
                print("right answer!!!")
                print("you escaped from the snake")
                return position[0], position[1], block
        elif(block == 19):
            if((turn==0 and question(tyu)==False)or turn==1):
                if(turn!=1):
                    print("wrong answer!!!")
                    print("you couldnt escape from the snake")
                if(turn==1):
                    print("computer bit by snake")
                return 665+x, 390+y, 7
            else:
                print("right answer!!!")
                print("you escaped from the snake")
                return position[0], position[1], block
        elif(block == 21):
            if((turn==0 and question(tyu)==False) or turn==1):
                if(turn!=1):
                    print("wrong answer!!!")
                    print("you couldnt escape from the snake")
                if(turn==1):
                    print("computer bit by snake")
                return 425+x, 390+y, 9
            else:
                print("right answer!!!")
                print("you escaped from the snake")
                return position[0], position[1], block
        elif(block == 27):
            if((turn==0 and question(tyu)==False)or turn==1):
                if(turn!=1):
                    print("wrong answer!!!")
                    print("you couldnt escape from the snake")
                if(turn==1):
                    print("computer bit by snake")
                return 65+x, 510+y, 1
            else:
                print("right answer!!!")
                print("you escaped from the snake")
                return position[0], position[1], block
        else:
            return position[0], position[1], block


class Display(object):
    def __init__(self,master,img,a1,a2,a3):

        #Create board of snake and ladder
        canvas_width = 850
        canvas_height = 600
        self.color = ["#FFF",   "#0FF"]
        self.canvas = Canvas(master, width = canvas_width, height = canvas_height, bg = "brown")
        self.canvas.grid(padx=0, pady=0)
        self.canvas.create_image(360,300,anchor=CENTER, image = img)

        self.x = 65
        self.y = 510
        self.m = []
        self.num_player = "Players"
        self.player = []
        self.position = []
        self.i = 0
        self.flag=0
        self.block=[]
        self.move = 1
        self.turn = 0
        self.qw=0

        self.xz=0
        self.b1=a1
        self.b2=a2
        self.b3=a3

        #Start Game


        self.zz = Label(self.canvas, text="enter option \n  0-don't reveal answer \n 1-reveal answer",
                           background='white', font=("Helvetica", 10))
        self.zz.place(x=720, y=165)
        self.newb=Button(self.canvas, text="1", background='white', command = self.ytu1, font=("Helvetica"))
        self.newb.place(x=720, y=245)
        self.newb1=Button(self.canvas, text="0", background='white', command = self.ytu, font=("Helvetica"))
        self.newb1.place(x=720, y=220)
        self.startGame = Button(self.canvas, text="Start", background='white', command = self.startGame, font=("Helvetica"))
        self.startGame.place(x=770, y=400)

    def ytu(self):
        self.qw=0
        #print("********",self.qw)
    def ytu1(self):
        self.qw=1
        #print("********",self.qw)

    def startGame(self):
            #Screen
            self.canvas.create_rectangle(810, 150, 760, 100, fill='white', outline='black')
            self.canvas.pack(fill=BOTH, expand=1)
            #Button
            self.diceRoll = Button(self.canvas, text="Roll",background='white',
                                   command = self.gamePlay, font=("Helvetica"))
            self.num_player = 2
            self.diceRoll.place(x=770, y=165)
            self.create_peice()
            self.startGame.place(x=-30, y=-30)
            self.newb.place(x=-280, y=-280)
            self.newb1.place(x=-380, y=-380)
            self.zz.place(x=-480,y=-480)


    def get_choice(self, value):
        self.num_player = value


    def diceMove(self, position, turn):
        move = dice()
        #move = 1
        #Print Dice Value to screen
        if(turn!=0):
            print( "computer roLLed!!! ",move)
        else:
            print("user rolled!!! ",move)
        dice_value = Label(self.canvas, text=str(move),
                           background='white', font=("Helvetica", 25))
        dice_value.pack()
        dice_value.place(x=775, y=105)


        self.x, self.y = position[0], position[1]
        self.move = move
        if(move+self.block[turn] > 30):
            time.sleep(0.70)
            return [self.x, self.y]


        self.block[turn] += move

        self.canvas.delete(self.player[turn])
        self.peices(move, turn)

        return [self.x, self.y]

    def peices(self, move, turn):
        #Starting value of and x and y should be 120 and 120
        #In create_circle initial value of x and y should be 100 and 550
        #To reach to the last block x should be 5*x and y should be 4*y
        #X should be added to value and Y should be subtracted
        # 5x120=600 and 4*120=480
        #m is the constant that tells which side to move i.e. left to right or right to left
        for i in range(move,0,-1):
            self.x = self.x+120*self.m[turn]

            if(self.x>665 and turn < 3):
                self.y = self.y - 120
                self.x = 665
                self.m[turn] = -1
            elif(self.x>700 and turn >=3):
                self.y = self.y - 120
                self.x = 700
                self.m[turn] = -1
            if(self.x<65 and turn < 3):
                self.x = 65
                self.y -= 120
                self.m[turn] = 1
            elif(self.x<100 and turn >=3):
                self.x = 100
                self.y -= 120
                self.m[turn] = 1
            if(self.y<30):
                self.y=30

            # Code For the Animation of piece
            self.canvas.delete(self.player[turn])
            self.player[turn] = self.canvas.create_circle(self.x, self.y, 15, fill=self.color[turn], outline=self.color[turn])
            self.canvas.update()
            time.sleep(0.60)
        if(turn!=0):
            print( "computer moved to ",self.block[turn])
        else:
            print("user moved to ",self.block[turn])
        ghj=self.qw
        self.x, self.y, self.block[turn] = MatchPosition().find_snake_or_ladder(self.block[turn], turn, [self.x, self.y],ghj)

        if(any(self.y == ai for ai in [390, 425, 460, 150, 185, 220])):
            self.m[turn] = -1
        else:
            self.m[turn] = 1
        if(turn!=0):
            print( "computer moved to ",self.block[turn])
        else:
            print("user moved to ",self.block[turn])

        self.canvas.delete(self.player[turn])
        self.player[turn] = self.canvas.create_circle(self.x, self.y, 15, fill=self.color[turn], outline="")


    def create_peice(self):
        for i in range(int(self.num_player)):
            self.player.append(self.canvas.create_circle(self.x, self.y, 15, fill=self.color[i], outline=""))
            self.position.append([self.x, self.y])
            self.m.append(1)
            self.block.append(1)
            self.y += 35


    def gamePlay(self):
        if(self.move == 6):
            turn = self.turn
        else:
            turn = self.i%self.num_player
            self.i += 1
            self.turn = turn
        self.position[turn] = self.diceMove(self.position[turn], turn)
        if(self.block[self.turn] >= 30):
            self.flag=1
            self.diceRoll.place(x=-30, y=-30)
            top = Toplevel()
            top.title("Snake and Ladder")
            if(self.turn==0):
                message = "user won "
                print("user won")
                q1,q2=ert(0)
            else:
                message="computer won"
                q1,q2=ert(1)
                print("computer won")
            msg = Message(top, text=message)
            top.geometry("%dx%d%+d%+d" % (100, 100, 250, 125))
            msg.pack()
            button = Button(top, text="Dismiss", command=top.destroy)
            button.pack()
            if(q1==2):
                print("regno:",self.b1)
                print("name:",self.b2)
                print("sec",self.b3)
                if(q2>=7):
                    print("your score is ",q2)
                    print("your general knowledge is excellent")
                elif(q2<7 and q2>=5):
                    print("your score is ",q2)
                    print("your general knowledge is good")
                else:
                    print("your score is ",q2)
                    print("your general knowledge is bad")
        time.sleep(0.60)
        if(((self.turn==0 and self.move!=6 )or(self.turn==1 and self.move==6 ))and self.flag==0):
            self.gamePlay()
