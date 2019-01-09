import tkinter as tk  
from PIL import Image,ImageTk  
root = tk.Tk()  
root.title("display image")  
im=Image.open("test.jpg")  
photo=ImageTk.PhotoImage(im)  
cv = tk.Canvas()  
cv.pack(side='top', fill='both', expand='yes')  
cv.create_image(50, 50, image=photo, anchor='nw')  
root.geometry("500x500")
root.mainloop()
