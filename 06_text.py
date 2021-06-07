import tkinter as tk

window = tk.Tk()

text_box = tk.Text()
text_box.pack()

text_box.insert("1.0", "Hello")
text_box.insert("2.0", "\nWorld")

#text_box.get("1.0", "1.5")
#text_box.get("1.0", tk.END)

#text_box.delete("1.0", "1.4")
#text_box.delete("1.0", tk.END)

#text_box.insert(tk.END, "Put me at the end!")
#text_box.insert(tk.END, "\nPut me on a new line!")

window.mainloop()
