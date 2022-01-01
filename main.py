from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title('TextPad')
root.geometry("1200x660")

# Create Main Frame
my_frame = Frame(root)
my_frame.pack(pady=5)

# Create our Scrollbar Fot the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)

# Create Text Box
my_text = Text(my_frame, width=1200, height=660, font=("Helvetica", 16), selectbackground="yellow", selectforeground="black", undo=True, yscrollcommand=text_scroll.set)
my_text.pack()

# Configure our Scrollbar
text_scroll.config(command=my_text.yview)

root.mainloop()