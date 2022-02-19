import random
(p1,p2) = (0,0) #scores of the 2 players. p1(White) has the rook (R) and the bishop (B) while p2(Black) has the queen (Q)

for i in range(100):

    Qrow=random.randint(0,7)  #placing queen on a random position on an 8*8 chessboard
    Qcol=random.randint(0,7)

    Rrow=random.randint(0,7)
    Rcol=random.randint(0,7)
    while ( (Qrow == Rrow) and (Qcol == Rcol)):  #Checking if Rook got the same position
        Rrow=random.randint(0,7)
        Rcol=random.randint(0,7)


    Brow=random.randint(0,7)
    Bcol=random.randint(0,7)
    while ( ( (Brow == Rrow) and (Bcol == Rcol) ) or ( (Brow == Qrow) and (Bcol == Qcol) ) ): #Same as ln12
        Brow=random.randint(0,7)
        Bcol=random.randint(0,7)


    if ( (Rrow == Qrow) or (Rcol == Qcol) ):  #if Rook captures the Queen, the the queen captures rook too. So +1 point to both.
        p1 += 1
        p2 += 1

    if ( (Qrow == Brow) or (Qcol == Bcol) ): #Queen captures Bishope
        p2 += 1

    if ( abs(Qrow-Brow) == abs(Qcol - Bcol)): #Bishop Captures Queen and vice versa (+1p to both)
        p1 += 1
        p2 += 1

print(" ------------------------------------\n                Score\n  P1(White): ", p1, "   P2(black): ", p2 ,'\n ------------------------------------\n' )

