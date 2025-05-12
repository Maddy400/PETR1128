import tkinter

#Create the window
window = tkinter.Tk()
#Set size of window
window.geometry("300x400")
#Set the title to Calculator
window.title("Calculator")

#Create text input
text_input_result = tkinter.Entry(window, font = ("Ariel",30))
#Use grid to set out the window
text_input_result.grid(row = 0, column = 0, columnspan = 3)

#Create memory variable for memory storage
memory = 0 

#Create function to see what button has been clicked
def button_click_input(num):
    #Get result of button
    current_number = text_input_result.get()
    #Delete the previous number
    text_input_result.delete(0, tkinter.END)
    #Puts the two numbers together so they appear next to each other. Using them as a string avoids the numbers being added together
    text_input_result.insert(0, str(current_number) + str(num))

#Clears the input bar
def button_clear_input():
    text_input_result.delete(0, tkinter.END)

#Create add to memory function
def button_add_to_memory():
    #Make memory accessible within the function
    global memory
    try:
        #Store the user input in the memory variable
        memory = int(text_input_result.get())
        #Deletes the input from the display
        text_input_result.delete(0, tkinter.END)
    except:
        #Deletes the input from the display
        text_input_result.delete(0, tkinter.END)
        #Dsplays an error message
        text_input_result.insert(0, "Error")

#Create memory recall function
def button_memory_recall():
    #Make memory accessible within the function
    global memory
    #Deletes the input form the display
    text_input_result.delete(0, tkinter.END)
    #Inserts what is stored in the memory
    text_input_result.insert(0, str(memory))

#Create memory clear function
def button_memory_clear():
    #Make memory accessible within the function
    global memory
    #Set memory to 0
    memory = 0
    #Delete the user input from the display
    text_input_result.delete(0, tkinter.END)

#Create function to add numbers
def button_add_input():
    first_input = text_input_result.get()
    #Make the first number inputted a global variable to be accessed in other functions
    global first
    #Make the symbol a global variable to be accessed in the equals function
    global symbol
    #Define the symbol
    symbol = "add"
    #Save the first number inputted in the variable 'first'
    first = int(first_input)
    #Deletes the input from the input bar
    text_input_result.delete(0, tkinter.END)

#Create function to subtract
def button_subtract_input():
    first_input = text_input_result.get()
    #Make the first number inputted a global variable to be accessed in other functions
    global first
    #Make the symbol a global variable to be accessed in the equals function
    global symbol
    #Define the symbol
    symbol = "subtract"
    #Save the first number inputted in the variable 'first'
    first = int(first_input)
    #Deletes the input from the input bar
    text_input_result.delete(0, tkinter.END)

#Create function to multiply
def button_multiply_input():
    first_input = text_input_result.get()
    #Make the first number inputted a global variable to be accessed in other functions
    global first
    #Make the symbol a global variable to be accessed in the equals function
    global symbol
    #Define the symbol
    symbol = "multiply"
    #Save the first number inputted in the variable 'first'
    first = int(first_input)
    #Deletes the input from the input bar
    text_input_result.delete(0, tkinter.END)

#Create function to divide
def button_divide_input():
    first_input = text_input_result.get()
    #Make the first number inputted a global variable to be accessed in other functions
    global first
    #Make the symbol a global variable to be accessed in the equals function
    global symbol
    #Define the symbol
    symbol = "divide"
    #Save the first number inputted in the variable 'first'
    first = int(first_input)
    #Deletes the input from the input bar
    text_input_result.delete(0, tkinter.END)

#Create function to calculate answer
def button_equal_input():
    #Retrieve the second input
    second_input = text_input_result.get()
    #Delete from the input bar
    text_input_result.delete(0, tkinter.END)

    #If statements to determine what action to perform
    if symbol == "add":
        text_input_result.insert(0, first + int(second_input))
    
    elif symbol == "subtract":
        text_input_result.insert(0, first - int(second_input))
    
    elif symbol == "divide":
        text_input_result.insert(0, first / int(second_input))
    
    elif symbol == "multiply":
        text_input_result.insert(0, first * int(second_input))
    
    else:
        print("Error")

#Create buttons
button_1 = tkinter.Button(window, text = "1", padx = 20, pady = 20, command = lambda: button_click_input(1))
button_2 = tkinter.Button(window, text = "2", padx = 20, pady = 20, command = lambda: button_click_input(2))
button_3 = tkinter.Button(window, text = "3", padx = 20, pady = 20, command = lambda: button_click_input(3))

button_4 = tkinter.Button(window, text = "4", padx = 20, pady = 20, command = lambda: button_click_input(4))
button_5 = tkinter.Button(window, text = "5", padx = 20, pady = 20, command = lambda: button_click_input(5))
button_6 = tkinter.Button(window, text = "6", padx = 20, pady = 20, command = lambda: button_click_input(6))

button_7 = tkinter.Button(window, text = "7", padx = 20, pady = 20, command = lambda: button_click_input(7))
button_8 = tkinter.Button(window, text = "8", padx = 20, pady = 20, command = lambda: button_click_input(8))
button_9 = tkinter.Button(window, text = "9", padx = 20, pady = 20, command = lambda: button_click_input(9))

button_0 = tkinter.Button(window, text = "0", padx = 20, pady = 20, command = lambda: button_click_input(0))
button_add = tkinter.Button(window, text = "+", padx = 20, pady = 20, command = button_add_input)
button_equals = tkinter.Button(window, text = "=", padx = 70, pady = 20, command = button_equal_input)
button_clear = tkinter.Button(window, text = "Clear All", padx = 60, pady = 20, command = button_clear_input)
button_subtract = tkinter.Button(window, text = "-", padx = 20, pady = 20, command = button_subtract_input)
button_multiply = tkinter.Button(window, text = "*", padx = 20, pady = 20, command = button_multiply_input)
button_divide = tkinter.Button(window, text = "/", padx = 20, pady = 20, command = button_divide_input)

button_memory_add = tkinter.Button(window, text = "M+", padx = 20, pady = 20, command = button_add_to_memory)
button_recall_memory = tkinter.Button(window, text = "MR", padx = 20, pady = 20, command = button_memory_recall)
button_clear_memory = tkinter.Button(window, text = "M", padx = 20, pady = 20, command = button_memory_clear)


#Place buttons using the grid
button_1.grid(row = 3,column = 0, sticky = "nsew")
button_2.grid(row = 3,column = 1, sticky = "nsew")
button_3.grid(row = 3,column = 2, sticky = "nsew")

button_4.grid(row = 2,column = 0, sticky = "nsew")
button_5.grid(row = 2,column = 1, sticky = "nsew")
button_6.grid(row = 2,column = 2, sticky = "nsew")

button_7.grid(row = 1,column = 0, sticky = "nsew")
button_8.grid(row = 1,column = 1, sticky = "nsew")
button_9.grid(row = 1,column = 2, sticky = "nsew")

button_0.grid(row = 4,column = 0, sticky = "nsew")
button_clear.grid(row = 4, column = 1, columnspan = 2, sticky = "nsew")
button_add.grid(row = 5, column = 0, sticky = "nsew")
button_equals.grid(row = 5, column = 1, columnspan = 2, sticky = "nsew")
button_subtract.grid(row=6, column= 0, sticky = "nsew")
button_multiply.grid(row=6, column= 1, sticky = "nsew")
button_divide.grid(row=6, column= 2, sticky = "nsew")

button_memory_add.grid(row=7, column= 0, sticky = "nsew")
button_recall_memory.grid(row=7, column= 1, sticky = "nsew")
button_clear_memory.grid(row=7, column= 2, sticky = "nsew")

#Run the window
window.mainloop()
