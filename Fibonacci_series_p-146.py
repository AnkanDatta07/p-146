# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 12:33:25 2022

@author: Ankan Datta
"""

from tkinter import *
root = Tk()

root.title("FIBONACCI SERIES")
root.geometry("400x400")
 
label_series = Label(root, text = "Fibonacci series : ")
input1 = Entry(root)
label_spiral = Label(root)

def Fibonacci():
    num = int(input1.get)
    first_no = 0
    second_no = 1
    sum = 0
    sum2 = 0
    counter = 1
    while (counter <= num):
        sum2 = sum2 + sum
        counter += 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        label_series["text"] += str(sum2) + ""
        label_spiral["text"] = "Fibonacci Sum : " + str(sum2)
        
btn = Button(root, text="Show Fibonacci Series", command = Fibonacci, bg = 'blue')

btn.pack()
input1.pack()
label_series.pack()
label_spiral.pack()

root.mainloop()