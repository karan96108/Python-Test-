from tkinter import *
from tkinter import filedialog

def open_file():
    file_path= filedialog.askopenfilename(filetypes=[("Text Files","*.txt")])
    if file_path:
        with open(file_path,"r") as file:
            text= file.read()
            text_area.delete('1.0',END)
            text_area.insert(END,text)
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")            
    if file_path:
        with open(file_path,"w") as file:
            text = text_area.get('1.0',END)
            file.write(text)
root = Tk()
root.title("NotePad")
root.geometry("500x500")




text_area = Text(root,width=190,height=90)
text_area.pack()

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

root.config(menu=menu_bar)
root.mainloop()