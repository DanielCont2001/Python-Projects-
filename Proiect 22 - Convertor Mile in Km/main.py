from tkinter import *
from turtle import color

window = Tk()
window.title("Convertor Mile in Km")
window.config(padx=25,pady=25)

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)

miles_label = Label(text="Mile")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="este egal cu = ")
is_equal_label.grid(column=0,row=1)

kilometers_result_label = Label(text = "0 Kilometri")
kilometers_result_label.grid(column=1,row=1)

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilometers_result_label.config(text=f"{km} kilometri")

calculate_button = Button(text="Calculeaza",command=miles_to_km)
calculate_button.grid(column=1,row=2) 








window.mainloop()