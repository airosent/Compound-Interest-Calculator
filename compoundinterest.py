from tkinter import *


#First, create a function that will reset all of the text fields in the calculator
def reset_calculator():
    '''Function that will delete each field's previous inputs to reset it for
    another calculation'''
    principal_box.delete(0, END)
    rate_box.delete(0, END)
    number_box.delete(0, END)
    time_box.delete(0, END)
    calculation_box.delete(0, END)
    principal_box.focus_set() #focus on the principal interest

def compound_interest():
    '''Function that does the actual calculation of the compound interest.'''
    principal = float(principal_box.get()) #get principal interest
    rate_of_interest = float(rate_box.get()) #get rate of interest
    number = float(number_box.get()) #get number of payments
    time = float(time_box.get()) #get the years it will take

    initial_calculation = principal * pow((1 + (rate_of_interest / (100 * number))), number * time) #actual calculation
    end_calculation = initial_calculation - principal #final compound interest amount
    calculation_box.insert(10, end_calculation) #insert the calculation into the result box


# main function
if __name__ == "__main__":
    UI = Tk()
    UI.title("Compound Interest Calculator") #title of the window
    UI.geometry("600x600+650+350") #sizing the window
    UI.resizable(0, 0) #not resizable because it just doesn't make sense for this project
    UI.configure(bg="lightblue") #background is light blue

    title_label = Label(
        UI,
        text="COMPOUND INTEREST\nCALCULATOR\n", #calculator title in bold
        font=("Arial bold", 25),
        fg="#211600",
        bg="lightblue"
    )
    title_label.place( #centering the title
        x=100,
        y=30
    )

    principal_label = Label(
        UI, #principal amount text label info
        text="Principal Amount:",
        font=("Arial", 12),
        bg="lightblue",
        fg="black"
    )
    rate_label = Label( #rate text label info
        UI,
        text="Rate of Interest (%):",
        font=("Arial", 12),
        bg="lightblue",
        fg="black"
    )
    payments_label = Label( #number of payments text label info
        UI,
        text="Number of Payments:",
        font=("Arial", 12),
        bg="lightblue",
        fg="black"
    )
    time_label = Label( #time period text label info
        UI,
        text="Time Period (Years):",
        font=("Arial", 12),
        bg="lightblue",
        fg="black"
    )

    calculation_label = Label( #compound interest text label info
        UI,
        text="Compound Interest:",
        font=("Arial", 12),
        bg="lightblue",
        fg="black"
    )

    principal_label.place(x=92, y=160) #centering and positioning labels
    rate_label.place(x=92, y=200)
    payments_label.place(x=92, y=240)
    time_label.place(x=92, y=280)
    calculation_label.place(x=92, y=380)

    principal_box = Entry(  #creating entry box for principal amount
        UI,
        font=("Arial", 12),
        bg="#fcf9e8",
        fg="#211600"
    )

    rate_box = Entry( #creating entry box for rate of interest
        UI,
        font=("Arial", 12),
        bg="#fcf9e8",
        fg="#211600"
    )

    number_box = Entry( #creating entry box for number of payments
        UI,
        font=("Arial", 12),
        bg="#fcf9e8",
        fg="#211600"
    )

    time_box = Entry( #creating entry box for number of years
        UI,
        font=("Arial", 12),
        bg="#fcf9e8",
        fg="#211600"
    )

    calculation_box = Entry( #creating entry box for the end result calculation
        UI,
        font=("Arial", 12),
        bg="#fcf9e8",
        fg="#211600"
    )

    principal_box.place(x=250, y=160) #positioning boxes next to their respective labels
    rate_box.place(x=250, y=200)
    number_box.place(x=250, y=240)
    time_box.place(x=250, y=280)
    calculation_box.place(x=250, y=380)

    result_button = Button( #creating a button to calculate the results
        UI,
        text="CALCULATE",
        font=("Arial bold", 9),
        bg="yellow",
        fg="black",
        command=compound_interest
    )

    reset_button = Button( #creating a reset button so users can reset their calculation
        UI,
        text="RESET",
        font=("Arial bold", 9),
        bg="orangered",
        fg="black",
        command=reset_calculator
    )

    result_button.place(x=300, y=330) #placing the buttons on the UI
    reset_button.place(x=320, y=430)

    UI.mainloop() #run window