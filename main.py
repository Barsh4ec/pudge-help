from tkinter import *
from answers import answer


tk = Tk()
tk.geometry("300x50+1650+980")
tk.overrideredirect(True)
tk.configure(bg="#FFFFFF")
tk.wm_attributes('-transparentcolor', '#FFFFFF')


# функція, яка читає буфер
def read(e):
    buffer = tk.clipboard_get()
    try:
        buffer_data['text'] = answer[buffer]
    except KeyError:
        buffer_data['text'] = "wrong input"


def quit(event):
    global flag
    if flag:
        tk.attributes('-topmost', False)
        flag = False
    else:
        tk.attributes('-topmost', True)
        flag = True


buffer_data = Label(tk, text="No Data", font='Aerial 5', bg="#FFFFFF", fg="#cdd0d4")
buffer_data.pack()


button = Button(tk, text="Read", font='Aerial 5', bg="#FFFFFF", fg="#cdd0d4", bd=10,
                highlightthickness=4, highlightcolor="#37d3ff", highlightbackground="#37d3ff", borderwidth=0)
button.pack()
button.bind("<Button-1>", read)

flag = True
tk.bind('<Control-z>', quit)
tk.attributes('-topmost', True)

tk.mainloop()
