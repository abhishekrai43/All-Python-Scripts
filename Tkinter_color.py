import pyautogui, PIL
import tkinter as tk
from threading import Thread

def cursorpixel():
    x,y = pyautogui.position()
    pixel = (x,y,x+1,y+1)
    grabColor(pixel)

def grabColor(square, max_colors=256):
    global color_label,root
    img=PIL.ImageGrab.grab(square)
    color = img.getcolors(max_colors)
    color_label.config(text=color)

def refresh():
    while True:
        cursorpixel()

def main():
    global color_label,root
    root=tk.Tk()
    root.minsize(150, 50)
    color_label = tk.Label(root,
                     fg = "black",
                     font = "Arial")
    color_label.pack()
    Thread(target=refresh).start()
    root.mainloop()


if __name__ == "__main__":
    main()