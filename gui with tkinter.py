import tkinter

window = tkinter.Tk()
window.minsize(width=500,height=300)

label = tkinter.Label(text="I am a label")
label.pack()

def gui_button():
    label.config(text="i am changed")

button = tkinter.Button(text="click me",command=gui_button)
button.pack()

input1 = tkinter.Entry(width=10)
input1.pack()

def gui_txt():
    label.config(text=input1.get())


button2 = tkinter.Button(text="get text",command=gui_txt)
button2.pack()  


window.mainloop()