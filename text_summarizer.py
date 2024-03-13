import os
from tkinter import END, Canvas, Label, PhotoImage, Tk,Button,Frame, Image
from tkinter import scrolledtext as st
from summarizer import summarizer as s
from keywords import keywords as k
import tkinter.messagebox as msg

basedir = os.path.dirname(__file__)
root = Tk()
root.resizable(True,True)
root.title("Text Summarizer")
img = Image("photo", file=os.path.join(basedir, "Images", "file.png"))
root.tk.call('wm','iconphoto', root._w, img)
bg = PhotoImage(file=os.path.join(basedir, "Images", "bgimg3.png"))
bg2 = PhotoImage(file=os.path.join(basedir, "Images", "1_08p8_RaBob1fVCc_ug4-UA.png"))
canvas1 = Canvas(root)
canvas1.grid()
canvas1.create_image(200, 260, image = bg, anchor = "center")
frame1 = Frame(canvas1)
Label(frame1, text ="Input", font=('arial', 20, 'bold'), fg = "red").grid(row = 0, column = 0)
text_area = st.ScrolledText(frame1, width = 50, height = 20, font = ("Times New Roman", 15))
text_area.grid(row = 1, column = 0, sticky = "s")
# text_area.config(background = "#000")
frame1.grid(row = 0, column = 0, pady = 10, padx = 10, sticky="nsew")
# frame1.config(background = "black")
text_area.focus()

frame2 = Frame(canvas1)
Label(frame2, text ="Output", font=('arial', 20, 'bold'), fg = "red").grid(row = 0, column = 0)
summ_area = st.ScrolledText(frame2, width = 50, height = 20, font = ("Times New Roman", 15))
summ_area.grid(row = 1, column = 0, sticky = "s")
# summ_area.config(foreground = "red", background = "black")
frame2.grid(row = 0,column = 1, pady = 10, padx = 10,sticky="nsew")

##performing summarization of the text
def summ():
    txt = text_area.get("0.0","end")
    # msg.showerror("Parsing Error", "Please type input first.",icon = "error")
    text = s()
    txt1 = text.txt_summ(txt)
    summ_area.insert("0.0",txt1)
    summ_area.focus()
    summ_area.configure(state="disabled")

##Clearing the text areas
def clear():
    summ_area.configure(state="normal")
    text_area.delete("0.0","end")
    summ_area.delete("0.0","end")

##Destroy the window 1 elements
def des():
    frame1.destroy()
    frame2.destroy()
    btn1.destroy()
    btn3.destroy()
    canvas1.destroy()

##keyword finding function
def keywords():
    des()
    root.title("Text Keywords Extractor")
    canvas2 = Canvas(root)
    canvas2.grid()
    canvas2.create_image(425, 140, image = bg2, anchor = "center")
    frame3 = Frame(canvas2)
    Label(frame3, text ="Input", font=('arial', 20, 'bold'), fg = "red").grid(row = 0, column = 0)
    text_area2 = st.ScrolledText(frame3, width = 50, height = 20, font = ("Times New Roman", 15))
    text_area2.grid(row = 1, column = 0, sticky = "s")
    frame3.grid(column = 0, pady = 10, padx = 10 ,sticky="nsew")
    text_area2.focus()

    frame4 = Frame(canvas2)
    Label(frame4, text ="Ouput", font=('arial', 20, 'bold'), fg = "red").grid(row = 0, column = 0)
    summ_area2 = st.ScrolledText(frame4, width = 50, height = 20, font = ("Times New Roman", 15))
    summ_area2.grid(row = 1, column = 0, sticky = "s")
    frame4.grid(row = 0,column = 1, pady = 10, padx = 10,sticky="nsew")
    
    def res():
        txt = text_area2.get("0.0","end")
        # if txt == "":
        #     msg.showinfo("Parsing Error", "Please type input first.")
        text = k()
        txt1 = text.key(txt)
        summ_area2.insert("0.0",txt1)
        summ_area2.focus()
        summ_area2.configure(state="disabled")

    def clear():
        summ_area2.configure(state="normal")
        text_area2.delete("0.0","end")
        summ_area2.delete("0.0","end")

    btn4 = Button(canvas2, text="Keywords", width=6, height=2, font=("arial",15, "bold"), command=lambda:[res()])
    btn4.grid(row = 1, column = 0, pady = 10, padx = 10, sticky="e")
    btn5 = Button(canvas2,text="Clear", width=6, height=2, font=("arial",15, "bold"), command=lambda:[clear()])
    btn5.grid(row = 1, column = 1, pady = 10, padx = 10, sticky="w")


btn1 = Button(canvas1, text="Summarize", width=6, height=2, font=("arial",15, "bold"), command=lambda:[summ()])
btn1.grid(row = 1, column = 0, pady = 10, padx = 10, sticky="e")
btn2 = Button(canvas1,text="Clear", width=6, height=2, font=("arial",15, "bold"), command=lambda:[clear()])
btn2.grid(row = 1, column = 1, pady = 10, padx = 10, sticky="w")
btn3 = Button(canvas1,text="Keywords Finder", width=12, height=2, font=("arial",15, "bold"), command=lambda:[keywords()])
btn3.grid(row = 2, column = 0, columnspan = 2, pady = 10, padx = 10)
root.mainloop()