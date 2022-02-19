import random

xartia = []
figures = ["J", "Q", "K"]
xarti = [i for i in range(1, 11)] + figures
color = ["H", "S", "C", "D"]
p1count = 0
p2count = 0
drawcount = 0
for i in range(100):
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    random.shuffle(xartia)
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        #print(sum1)
    if sum1>21:
        p2count = p2count + 1
        #print("P2 wins!")
    else:
        # print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
             #print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
           # print("P1 wins!")
            p1count = p1count + 1
        elif sum2>sum1:
           # print("P2 wins!")
            p2count = p2count + 1
        else:
            # print("draw!")
            drawcount = drawcount + 1
print("In 100 rounds the score is: ", "\n p1: ", p1count, "\n p2: ", p2count, "\n draw: ", drawcount)


print ("\n ------------------------------------------------------ \n")


p1count = 0
p2count = 0
drawcount = 0
for i in range(100):
    for i in xarti:
        for j in color:
            xartia.append([i,j])
    copy=xartia[:51]
    random.shuffle(copy)
    xartia[:51] = copy 
    player1=[]
    sum1=0
    while sum1<16:
        sum1=0
        player1.append(xartia.pop())
        # print (player1)
        for card in player1:
            if card[0] in figures:
                sum1=sum1+10
            else:
                sum1=sum1+card[0]
        #print(sum1)
    if sum1>21:
        p2count= p2count+1
        #print("P2 wins!")
    else:
        #print("P2 joins the game") #let me add one more player
        player2=[]
        sum2=0
        while ((xartia[-1][0] == 10) or (xartia[-1][0] in figures)):
            random.shuffle(xartia)
        while sum2<16:
            sum2=0
            player2.append(xartia.pop())
            # print (player2)
            for card in player2:
                if card[0] in figures:
                    sum2=sum2+10
                else:
                    sum2=sum2+card[0]
            #print(sum2)
        if sum2>21:
            sum2=0
        if sum1>sum2:
           # print("P1 wins!")
            p1count = p1count + 1
        elif sum2>sum1:
           # print("P2 wins!")
            p2count = p2count + 1
        else:
            # print("draw!")
            drawcount = drawcount + 1
print("Now, in 100 rounds the score is: ", "\n p1: ", p1count, "\n p2: ", p2count, "\n draw: ", drawcount)