import tkinter as tk
# I'd like to mention that a lot of this code was kinda inspired by https://github.com/Alok-2002/python_tkinter_projects/blob/main/CALCULATOR/CALCULATOR%20APP.py ! I haven't really messed with Tkinter before, so I'm using it as reference, kinda.
root=tk.Tk()
root.title("Calculator")
root.geometry("320x480")
root.resizable(False,False)
root.configure(bg="#191419")

top = ""

def clear():
    global top
    top = ""
    label.config(text=top)

def show_numbers(number):
    global top
    top+=number
    label.config(text=top)

def equation():
    global top
    answer = ""
    if top != "":
        try:
            answer = eval(top)
        except:
            answer = "Error!"
            top = ""
        label.config(text=answer)

label=tk.Label(root, width=17, height=1, text="",font=("Comic Sans MS",20), bg="#FFE0FF", fg="#000")
label.place(x=20,y=20)

tk.Button(root, text="0", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#332833", command=lambda: show_numbers("0")).place(x=94,y=385)
tk.Button(root, text="1", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#332833", command=lambda: show_numbers("1")).place(x=22,y=308)
tk.Button(root, text="2", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#332833", command=lambda: show_numbers("2")).place(x=94,y=308)
tk.Button(root, text="3", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#332833", command=lambda: show_numbers("3")).place(x=166,y=308)
tk.Button(root, text="4", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#332833", command=lambda: show_numbers("4")).place(x=22,y=231)
tk.Button(root, text="5", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#332833", command=lambda: show_numbers("5")).place(x=94,y=231)
tk.Button(root, text="6", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#332833", command=lambda: show_numbers("6")).place(x=166,y=231)
tk.Button(root, text="7", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#332833", command=lambda: show_numbers("7")).place(x=22,y=154)
tk.Button(root, text="8", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#332833", command=lambda: show_numbers("8")).place(x=94,y=154)
tk.Button(root, text="9", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#332833", command=lambda: show_numbers("9")).place(x=166,y=154)
tk.Button(root, text=".", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#332833", command=lambda: show_numbers(".")).place(x=166,y=385)
tk.Button(root, text="C", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#7F667F", command=lambda: clear()).place(x=22,y=77)
tk.Button(root, text="+", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#514051", command=lambda: show_numbers("+")).place(x=238,y=231)
tk.Button(root, text="-", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#514051", command=lambda: show_numbers("-")).place(x=238,y=154)
tk.Button(root, text="x", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#514051", command=lambda: show_numbers("*")).place(x=238,y=77)
tk.Button(root, text="/", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#514051", command=lambda: show_numbers("/")).place(x=166,y=77)
tk.Button(root, text="x²", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#514051", command=lambda: show_numbers("**2")).place(x=94,y=77)
tk.Button(root, text="π", font=("Comic Sans MS",20,), width=3, height=1, fg="#FFFFFF", bg="#332833", command=lambda: show_numbers("3.14")).place(x=22,y=385)
tk.Button(root, text="=", font=("Comic Sans MS",20,), width=3, height=3, fg="#FFFFFF", bg="#7F667F", command=lambda: equation()).place(x=238,y=308)

root.mainloop()