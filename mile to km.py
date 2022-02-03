import tkinter

window = tkinter.Tk()
window.minsize(width=200,height=200)
window.config(padx=20,pady=20)

text = tkinter.Label(text="is equal to ")
text.grid(column=0,row=2)
text2 = tkinter.Label(text="0")
text2.grid(column=3,row=2)
text3 = tkinter.Label(text="Km ")
text3.grid(column=4,row=2)
text4 = tkinter.Label(text="Miles")
text4.grid(column=4,row=1)

def gui_button():
    km = round(float(input1.get()) * 1.60934)
    text2.config(text=f"{km}")

button = tkinter.Button(text="Calculate",command=gui_button)
button.grid(column=3,row=3)

input1 = tkinter.Entry(width=10)
input1.grid(column=3,row=1)


window.mainloop()