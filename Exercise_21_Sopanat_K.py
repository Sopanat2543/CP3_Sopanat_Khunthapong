from tkinter import *
import math

def leftClickButton(event):
    bmi = round(float(textBoxWeight.get()) /math.pow(float(textBoxHeight.get())/100,2))
    print(bmi)
    if bmi > 30.0:
        labelResult.configure(text = f"{bmi} อ้วนมาก")
    elif 25.0 <= bmi <= 29.9:
        labelResult.configure(text = f"{bmi} อ้วน")
    elif 23.0 <= bmi <= 24.9:
        labelResult.configure(text = f"{bmi} น้ำหนักเกิน")
    elif 18.6 <= bmi <= 22.9:
        labelResult.configure(text = f"{bmi} น้ำหนักปกติ")
    elif bmi < 18.5:
        labelResult.configure(text = f"{bmi} ผอมเกินไป")
    

MainWindow = Tk()

labelHeight = Label(MainWindow, text = "ส่วนสูง (cm.)")
labelHeight.grid(row = 0, column = 0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row = 0, column = 1)

labelWeight = Label(MainWindow, text = "น้ำหนัก (kg.)")
labelWeight.grid(row = 1, column = 0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row = 1, column = 1)

calculateButton = Button(MainWindow, text = "คำนวน BMI")
calculateButton.grid(row = 2, column = 0)
calculateButton.bind("<Button-1>", leftClickButton)

labelResult = Label(MainWindow, text = "ผลลัพธ์")
labelResult.grid(row = 2, column = 1)

MainWindow.mainloop()
