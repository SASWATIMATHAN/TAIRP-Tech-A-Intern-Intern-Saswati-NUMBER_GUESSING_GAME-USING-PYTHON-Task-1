import random
from tkinter import *  

root = Tk()
root.title("Number guessing game")
root.geometry('400x400+50+50')

class NumberGuessing:
    #Variables_that_stores_Entry_values
    num1 = IntVar()
    num2 = IntVar()
    guessedNumber=IntVar()

    #It_stores_the_random_Number
    value=None

    #Function_For_Checking_And_Generating_Random_No
    def check(self):
        #If_No_value_is_entered
        if self.num1.get()==0 or self.num2.get() == 0 or self.guessedNumber.get() ==0 :
            self.ResultLabel.configure(text="Kindly fill in all required fields")
        else:
            #The_Line_Below_Generates_A_Random_No_And_Stores_It_In_value_Variable
            self.value = random.randint(self.num1.get(), self.num2.get())

            #Condition_that_checks_random_no_matches_guessed_no_or_not
            if self.guessedNumber.get() == self.value:

                #If_matches_result_label_text_changed_to_given_text
                self.ResultLabel.configure(text= "Just guessing like a wow! Good Job!")
            else:
                #If_not_matches_result_label_text_changed_to_given_text_and_random_no
                self.ResultLabel.configure(text="Sorry! Correct number is "+ str(self.value))

    #When_the_class_called_this_functions_runs_first
    def __init__(self):
        #Fonts_for_Label_&_Entry_Boxes
        self.lfont = ('Algerian', 16)
        
        #_Label_FROM
        self.Label1= Label(root, text="From", font=self.lfont, foreground="red")
        self.Label1.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        #Grid_Helps_the_Label_or_Any_Field_to_align_in_a_perfect_place
        #Such_as_In_row_or_column

        #Entry_Box_For_Storing_FROM_Value
        self.entry1= Entry(root, textvariable=self.num1, font=self.lfont, foreground="blue")
        self.entry1.grid(row=0, column=1, padx=5, pady=5)

        #_Label_TO
        self.Label2= Label(root, text="To", font=self.lfont, foreground="red")
        self.Label2.grid(row=1, column=0, sticky=W, padx=5, pady=5)

        #Entry_Box_For_Storing_TO_Value
        self.entry2= Entry(root, textvariable=self.num2, font=self.lfont, foreground="blue")
        self.entry2.grid(row=1, column=1, padx=5, pady=5)

        #Label_Guess_Any_Number
        self.Label3= Label(root, text="Guess Any Number", font=self.lfont, foreground="darkViolet")
        self.Label3.grid(row=3, columnspan=2, pady=10)

        #Entry_Box_For_Number_Guessing
        self.entry3= Entry(root, textvariable=self.guessedNumber, font=self.lfont, foreground="darkorchid")
        self.entry3.grid(row=4, columnspan=2, pady=10, padx=5)

        #Button_That_Check_The_Value_Matches_Random_No_OR_Not
        self.btn = Button(root, text="Check", font=self.lfont, foreground="darkviolet", command=self.check)
        self.btn.grid(row=5, columnspan=3, pady=10,)

        #Label_For_Showing_Result
        self.ResultLabel= Label(root, text="", font=self.lfont, foreground="darkViolet")
        self.ResultLabel.grid(row=6, columnspan=2, pady=10, padx=5)

        root.mainloop()

#Calling_The_Class
NumberGuessing()
