## #include랑 같은 내용 , *는 all 모두의 의미##
from tkinter import *

## 변수 초기화##
window=None
canvas = None
def mouseClick(event):
  global x1, y1
  x1=event.x
  y1=event.y
def mouseDrop(event):
  global x2,y2
  x2=event.x
  y2=event.y
  canvas.create_line(x1,y1,x2,y2,width=5,fill="red")
def mouseDrop2(event):
  global x3,y3
  x3=event.x
  y3=event.y
  canvas.create_line(x1,y1,x3,y3,width=5,fill="blue")


window=Tk() ## Tk 는 윈도우 프레임 만드는 함수##
window.title("직선만 되는 그림판")
canvas=Canvas(window, height=300, width = 300, background = "white")
canvas.bind("<Button-1>",mouseClick)
canvas.bind("<ButtonRelease-1>",mouseDrop2)
canvas.bind("<Button-3>",mouseClick)
canvas.bind("<ButtonRelease-3>",mouseDrop)
canvas.pack()
window.mainloop()
