import tkinter as tk
def SecondaryWindow(): 
    window = tk.Tk()
    window.title("Grid Manager")
    
    for x in range(20):
        for y in range(2):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
        frame.grid(row=x, column=y)  # line 13
        label = tk.Label(master=frame, text="hello world")
        label.pack()
    
    window.mainloop()
    