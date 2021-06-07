import tkinter as tk

window = tk.Tk()

window.columnconfigure(0, weight=1, minsize=75)
window.columnconfigure(1, weight=1, minsize=75)
window.columnconfigure(2, weight=1, minsize=74)

window.rowconfigure(0, weight=1, minsize=50)
window.rowconfigure(1, weight=1, minsize=50)
window.rowconfigure(2, weight=1, minsize=50)

for i in range(3):

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()