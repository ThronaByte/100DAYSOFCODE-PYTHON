from tkinter import Tk, Label, Entry, Button

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")

# # #Windows
windows = Tk()
windows.title("Miles To Km Converter")
windows.config(padx=20, pady=20)




# # #Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)




# Label
label = Label(text='Miles', font=('Arial',24))
label.grid(row=0,column=2)

# is equal
is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

# km_result
km_result = Label(text="0")
km_result.grid(row=1, column=1)

# km_label
km_label =Label(text="km")
km_label.grid(row=1, column=2)

# calc_button
calc_button = Button(text="Calculate", command=miles_to_km)
calc_button.grid(row=2, column=1)



windows.mainloop()