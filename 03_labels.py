import tkinter as tk

window = tk.Tk()

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",
    background="black"
)
label.pack()

label = tk.Label(text="Hello, Tkinter", background="#34A2FE")
label.pack()

label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10,
    height=10
)
label.pack()


window.mainloop()
