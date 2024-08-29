import tkinter as tk
import os

class ImageManager:
    def __init__(self):
        self.images = {}

    def add(self, name, path):
        self.images[name] = {'id': tk.PhotoImage(file=path), 'path': path}
        self.images[name]['id'].image = self.images[name]['id']

    def draw(self, name, x=0, y=0):
        self.images[name]['img'] = tk.Label(image=self.images[name]['id'])
        self.images[name]['img'].place(x=x, y=y)

    def undraw(self, name):
        self.images[name]['img'].destroy()

    def place(self, name, x, y):
        self.images[name]['img'].place(x=x, y=y)

def pathFromSelf(end_path:str) -> str:
    return __file__.replace("[name_here].py", end_path)