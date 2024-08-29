def testPG():
    try:
        import pygame
        del pygame
        return True
    except:
#         import tkinter as tk
#         from tkinter import messagebox as mb
#         root = tk.Tk()
#         root.geometry("0x0")
#         root.overrideredirect(1)
#         mb.showerror("LatT Loader", """Pygame import failed!
# Try using pip to install pygame!""")
#         root.destroy()
        return False

# def splash():
#     import tkinter as tk
#     from tkinter import ttk
#     from tkinter import messagebox as mb
#     from tkinter import filedialog as fd
#     from time import sleep

#     loading = tk.Tk()
#     loading.overrideredirect(1)
#     loading.eval('tk::PlaceWindow . center')
#     loading.config(cursor="wait", bg="black")

#     tk.Label(loading, text="Look at the Time Studios\n", font=("Helvetica", 22),
#             bg="black", fg="white").pack()

#     # progressbar
#     pb = ttk.Progressbar(
#         loading,
#         orient='horizontal',
#         #mode='indeterminate',
#         length=280
#     )
#     pb.pack()

#     tk.Label(loading, text="Please Wait...", font=("Helvetica", 10), bg="black"
#             , fg="white").pack()

#     for i in range(100):
#         sleep(0.01)
#         pb.step(1)
#         loading.update()

#     loading.destroy()

# def winPos(x, y):
#     import os
#     os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

# def _warning(text:str):
#     import tkinter as tk
#     from tkinter import messagebox as mb
#     root = tk.Tk()
#     root.geometry("0x0")
#     root.overrideredirect(1)
#     mb.showwarning("LatT Loader", text)
#     root.destroy()

# def _question(text:str):
#     import tkinter as tk
#     from tkinter import messagebox as mb
#     root = tk.Tk()
#     root.geometry("0x0")
#     root.overrideredirect(1)
#     out = mb.askyesno("LatT Loader", text)
#     root.destroy()
#     return out

# def betaWarning():
#     _warning("This game is in beta! Things may not work!")

# def run(title, iv, prompt="Enter Console Command"):
#     import tkinter as tk
#     from tkinter.simpledialog import askstring
#     root = tk.Tk()
#     root.geometry("0x0")
#     root.overrideredirect(1)
#     out = askstring(title, prompt=prompt, initialvalue=iv, parent=root)
#     root.destroy()
#     return out

# def askInt(title, prompt, iv):
#     import tkinter as tk
#     from tkinter.simpledialog import askstring
#     root = tk.Tk()
#     root.geometry("0x0")
#     root.overrideredirect(1)
#     out = askstring(title, prompt=prompt, initialvalue=iv, parent=root)
#     root.destroy()
#     return out