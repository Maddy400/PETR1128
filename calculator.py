import tkinter 
import math

# Create the window
window = tkinter.Tk()
window.geometry("320x500")
window.title("Calculator")
window.configure(bg = "white")

#Create text input
text_input_result = tkinter.Entry(window, font=("Ariel", 24))
text_input_result.grid(row=0, column=0, columnspan=4, sticky="nsew")

#Memory variable set to 0 at the beginning
memory = 0

#Create a function to retrive the input from the user
def button_click_input(value):
    current = text_input_result.get()
    text_input_result.delete(0, tkinter.END)
    text_input_result.insert(0, current + str(value))

#Create a function to clear the input bar
def button_clear_input():
    text_input_result.delete(0, tkinter.END)

#Create a function to add to the memory
def button_add_to_memory():
    #Make memory accessible within the function
    global memory
    try:
        #Store the user input in the memory variable
        memory = float(text_input_result.get())
        #Deletes the input from the display
        text_input_result.delete(0, tkinter.END)
    except:
        #Deletes the input from the display
        text_input_result.delete(0, tkinter.END)
        #Deletes the input from the display
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

#Set the inputs to each function to make the buttons work
def button_log():
    button_click_input("log(")

def button_sin():
    button_click_input("sin(")

def button_cos():
    button_click_input("cos(")

def button_tan():
    button_click_input("tan(")

def button_inverse_sin():
    button_click_input("asin(")

def button_inverse_cos():
    button_click_input("acos(")

def button_inverse_tan():
    button_click_input("atan(")

#Create the equals function to calculate
def button_equal_input():
    try:
        #Retrieve the input
        expression = text_input_result.get()
        #Create a result variable that calculates using the saved methods in the dictionary
        result = eval(expression, {"__builtins__": None}, {
            "math": math,
            "sqrt": math.sqrt,
            "sin": lambda x: math.sin(math.radians(x)),
            "cos": lambda x: math.cos(math.radians(x)),
            "tan": lambda x: math.tan(math.radians(x)),
            "acos": lambda x: math.acos(math.radians(x)),
            "asin": lambda x: math.asin(math.radians(x)),
            "atan": lambda x: math.atan(math.radians(x)),
            "log": lambda x: math.log10(x),
            "pi": math.pi,
            "e": math.e,
            "pow": pow
        })
        #Delete from the input bar
        text_input_result.delete(0, tkinter.END)
        #Displays the result
        text_input_result.insert(0, str(result))
    except Exception:
        #Deletes from the input bar
        text_input_result.delete(0, tkinter.END)
        #Displays an error message
        text_input_result.insert(0, "Error")
                 

#Create buttons
button_1 = tkinter.Button(window, text = "1", padx = 20, pady = 20, command = lambda: button_click_input(1), font=("Arial", 14))
button_2 = tkinter.Button(window, text = "2", padx = 20, pady = 20, command = lambda: button_click_input(2), font=("Arial", 14))
button_3 = tkinter.Button(window, text = "3", padx = 20, pady = 20, command = lambda: button_click_input(3), font=("Arial", 14))

button_4 = tkinter.Button(window, text = "4", padx = 20, pady = 20, command = lambda: button_click_input(4), font=("Arial", 14))
button_5 = tkinter.Button(window, text = "5", padx = 20, pady = 20, command = lambda: button_click_input(5), font=("Arial", 14))
button_6 = tkinter.Button(window, text = "6", padx = 20, pady = 20, command = lambda: button_click_input(6), font=("Arial", 14))

button_7 = tkinter.Button(window, text = "7", padx = 20, pady = 20, command = lambda: button_click_input(7), font=("Arial", 14))
button_8 = tkinter.Button(window, text = "8", padx = 20, pady = 20, command = lambda: button_click_input(8), font=("Arial", 14))
button_9 = tkinter.Button(window, text = "9", padx = 20, pady = 20, command = lambda: button_click_input(9), font=("Arial", 14))

button_0 = tkinter.Button(window, text = "0", padx = 20, pady = 20, command = lambda: button_click_input(0), font=("Arial", 14))
button_add = tkinter.Button(window, text = "+", padx = 20, pady = 20, command = lambda: button_click_input("+"), font=("Arial", 14))
button_equals = tkinter.Button(window, text = "=", padx = 70, pady = 20, command = button_equal_input, font=("Arial", 14))
button_clear = tkinter.Button(window, text = "Clear All", padx = 60, pady = 20, command = button_clear_input, font=("Arial", 14))
button_subtract = tkinter.Button(window, text = "-", padx = 20, pady = 20, command = lambda: button_click_input("-"), font=("Arial", 14))
button_multiply = tkinter.Button(window, text = "*", padx = 20, pady = 20, command = lambda: button_click_input("*"), font=("Arial", 14))
button_divide = tkinter.Button(window, text = "/", padx = 20, pady = 20, command = lambda: button_click_input("/"), font=("Arial", 14))

button_percentage = tkinter.Button(window, text = "%", padx = 20, pady = 20, command = lambda: button_click_input ("%"), font=("Arial", 14))
button_power_of = tkinter.Button(window, text = "^", padx = 20, pady = 20, command = lambda: button_click_input("**"), font=("Arial", 14))
button_square_root = tkinter.Button(window, text = "√", padx = 20, pady = 20, command = lambda: button_click_input("sqrt("), font=("Arial", 14))

button_decimal_point = tkinter.Button(window, text = ".", padx = 20, pady = 20, command = lambda: button_click_input("."), font=("Arial", 14))
button_bracket_open = tkinter.Button(window, text = "(", padx = 20, pady = 20, command = lambda: button_click_input("("), font=("Arial", 14))
button_bracket_close = tkinter.Button(window, text = ")", padx = 20, pady = 20, command = lambda: button_click_input(")"), font=("Arial", 14))

button_sin_ = tkinter.Button(window, text = "Sin", padx = 20, pady = 20, command = button_sin, font=("Arial", 14))
button_cos_ = tkinter.Button(window, text = "Cos", padx = 20, pady = 20, command = button_cos, font=("Arial", 14))
button_tan_ = tkinter.Button(window, text = "Tan", padx = 20, pady = 20, command = button_tan, font=("Arial", 14))

button_sin_inverse = tkinter.Button(window, text = "Asin", padx = 20, pady = 20, command = button_inverse_sin, font=("Arial", 14))
button_cos_inverse = tkinter.Button(window, text = "Acos", padx = 20, pady = 20, command = button_inverse_cos, font=("Arial", 14))
button_tan_inverse = tkinter.Button(window, text = "Atan", padx = 20, pady = 20, command = button_inverse_tan, font=("Arial", 14))

button_pi = tkinter.Button(window, text = "π", padx = 20, pady = 20, command = lambda: button_click_input(math.pi), font=("Arial", 14))
button_log_ = tkinter.Button(window, text = "Log", padx = 20, pady = 20, command = button_log, font=("Arial", 14))
button_e = tkinter.Button(window, text = "e", padx = 20, pady = 20, command = lambda: button_click_input(math.e), font=("Arial", 14))

button_memory_add = tkinter.Button(window, text = "M+", padx = 20, pady = 20, command = button_add_to_memory, font=("Arial", 14))
button_recall_memory = tkinter.Button(window, text = "MR", padx = 20, pady = 20, command = button_memory_recall, font=("Arial", 14))
button_clear_memory = tkinter.Button(window, text = "M", padx = 20, pady = 20, command = button_memory_clear, font=("Arial", 14))


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

button_power_of.grid(row=7, column= 0, sticky = "nsew")
button_percentage.grid(row=7, column= 1, sticky = "nsew")
button_square_root.grid(row=7, column= 2, sticky = "nsew")

button_decimal_point.grid(row=9, column = 0, sticky = "nsew")
button_bracket_open.grid(row=9, column = 1, sticky = "nsew")
button_bracket_close.grid(row=9, column = 2, sticky = "nsew")

button_sin_.grid(row=8, column= 0, sticky = "nsew")
button_cos_.grid(row=8, column= 1, sticky = "nsew")
button_tan_.grid(row=8, column= 2, sticky = "nsew")

button_sin_inverse.grid(row=10, column= 0, sticky = "nsew")
button_cos_inverse.grid(row=10, column= 1, sticky = "nsew")
button_tan_inverse.grid(row=10, column= 2, sticky = "nsew")

button_pi.grid(row=11, column= 0, sticky = "nsew")
button_log_.grid(row=11, column= 1, sticky = "nsew")
button_e.grid(row=11, column= 2, sticky = "nsew")

button_memory_add.grid(row=12, column= 0, sticky = "nsew")
button_recall_memory.grid(row=12, column= 1, sticky = "nsew")
button_clear_memory.grid(row=12, column= 2, sticky = "nsew")

#Run the window
window.mainloop()

