from graphics import*
p=[[0 for a in range(16)] for b in range(16)]
black=[[0 for a in range(16)] for b in range(16)]
white=[[0 for a in range(16)] for b in range(16)]
q=[[0 for a in range(15)] for b in range(15)]


win=GraphWin('five in a row',480,600)
win.setBackground('green')
def WinBoard():
    for i in range(15):
        for j in range(15):
            p[i][j]=Point(i*30+30,j*30+30)
            p[i][j].draw(win)
    for r in range(15):
        Line(p[r][0],p[r][14]).draw(win)
    for s in range(15):
        Line(p[0][s],p[14][s]).draw(win)
    center=Circle(p[7][7],3)
    center.draw(win)
    center.setFill('black')


def Click():
    p1=win.getMouse()
    x1=p1.getX()
    y1=p1.getY()
    for i in range(15):
        for j in range(15):
            sqrdis=((x1-p[i][j].getX())*(x1-p[i][j].getX()))+(y1-p[i][j].getY())*(y1-p[i][j].getY())
            if sqrdis<=200 and q[i][j]==0:
               if p[15][15]%2==0:
                    black[i+1][j+1]=1
                    q[i][j]=Circle(p[i][j],10)
                    q[i][j].draw(win)
                    q[i][j].setFill('black')
               if p[15][15]%2==1:
                    white[i+1][j+1]=1
                    q[i][j]=Circle(p[i][j],10)
                    q[i][j].draw(win)
                    q[i][j].setFill('white')
               p[15][15]+=1
def Check():
    for i in range(15):
        for j in range(11):
            if black[i+1][j+1] and black[i+1][j+2] and black[i+1][j+3] and black[i+1][j+4] and black[i+1][j+5]:
               return 1
               break
            if white[i+1][j+1] and white[i+1][j+2]and white[i+1][j+3]and white[i+1][j+4]and white[i+1][j+5]:
               return 2
               break
    for i in range(11):
        for j in range(15):
            if black[i+1][j+1] and black[i+2][j+1]and black[i+3][j+1]and black[i+4][j+1]and black[i+5][j+1]:
               return 1
               break
            if white[i+1][j+1] and white[i+2][j+1]and white[i+3][j+1]and white[i+4][j+1]and white[i+5][j+1]:
               return 2
               break
    for i in range(11):
        for j in range(11):
            if black[i+1][j+1] and black[i+2][j+2]and black[i+3][j+3]and black[i+4][j+4]and black[i+5][j+5]:
               return 1
               break
            if white[i+1][j+1] and white[i+2][j+2]and white[i+3][j+3]and white[i+4][j+4]and white[i+5][j+5]:
               return 2
               break
    for i in range(11):
        for j in range(15):
            if black[i+1][j+1] and black[i+2][j]and black[i+3][j-1]and black[i+4][j-2]and black[i+5][j-3]:
               return 1
               break
            if white[i+1][j+1] and white[i+2][j]and white[i+3][j-1]and white[i+4][j-2]and white[i+5][j-3]:
               return 2
               break

def main():
    WinBoard()
    while 1:
        Click()
        Check()
        if Check()==1:
            Text(Point(240,550),'the black wins').draw(win)
            break
        if Check()==2:
            Text(Point(240,550),'the white wins').draw(win)
            break
    win.getMouse()
main()

