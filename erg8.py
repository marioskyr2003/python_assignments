import random

"""
the function below mimicks a chessboard (with rows and cols making the dimentions of it), places the 2 figures on random positions 
and calculates the points via possible movements(100 rounds)

"""
def chessgame(rows,cols): 
    p1=0  #scores of 2 players (p1=rook p2=bishop)
    p2=0
    for i in range(100):

    

        Rrow=random.randint(1,rows) #choosing a random position for rook ---- Rrow = rook row
        Rcol=random.randint(1,cols) #Rcol = rook column


        Brow=random.randint(1,rows)  #choosing a random position for bishop ---- Brow = bishop row
        Bcol=random.randint(1,cols)  #Bcol = bishop column
        while ( (Rrow==Brow) and (Rcol == Bcol) ):  #checking if random chose the same position with R, then recalculates position of B
            Brow=random.randint(1,rows)
            Bcol=random.randint(1,cols)


           
        if ( (Rrow == Brow) or (Rcol == Bcol) ):  #Checking if rook captures bishop (p1 +1 point)
            p1 += 1
        if ( ( abs(Rrow-Brow) == abs(Rcol-Bcol) ) ): #Checking if bishop captures rook (p2 +1 point)
            p2 += 1


    print('Score on a',rows,'*',cols,'chessboard after 100 rounds\n','p1 =', p1, "p2= ", p2, '\n')


#calling the function for 3 different chessboards
chessgame(8,8)
chessgame(7,8)
chessgame(7,7)