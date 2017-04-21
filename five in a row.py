from graphics import*
p=[[0 for a in range(16)] for b in range(16)]

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
