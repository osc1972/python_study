from tkinter import *

root = Tk()
root.title("Nado GUI") # 제목

bnt1 = Button(root, text="버튼1")
bnt1.pack() # pack()을 해줘야 버튼이 생성됨

bnt2 = Button(root, padx=5, pady=10, text="버튼2")
bnt2.pack()

bnt3 = Button(root, padx=10, pady=5, text="버튼3")
bnt3.pack()

bnt4 = Button(root, width=10, height=3, text="버튼4")
bnt4.pack()

bnt5 = Button(root, fg="red", bg="yellow", text="버튼5")
bnt5.pack()

# photo = PhotoImage(file=r"C:\\Users\\dhtkd\\Documents\\GitHub\\python_study\\GUI_basic\\osm.gif")
# bnt6 = Button(root, image=photo)
# bnt6.pack()

def btncmd():
    print("버튼이 클릭되었어요")

bnt7 = Button(root, text="동작하는 버튼", command=btncmd)
bnt7.pack()



root.mainloop()
