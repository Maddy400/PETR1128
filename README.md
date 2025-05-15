# PETR1128
This program is a scientific calculator with many different features such as brackets, trigonometric functions, and constants such as pi and e

## Features
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Brackets
6. Sin / Asin
7. Cos / Acos
8. Tan / Atan
9. Square root
10. Power of
11. Log
12. Pi
13. Eulers Number (e)
14. Percentage
15. Decimal
16. Memory Add
17. Memory Recall
18. Memory Delete
19. 0 - 9
20. Clear all
21. Equals

![image](https://github.com/user-attachments/assets/a627aab6-916f-4184-a72d-47ff1acff5a3)

## Installation
To install and use this calculator:

1. Press "Code" and copy the URL
2. Open the terminal
3. Run the following: git clone https://github.com/Maddy400/PETR1128.git

Alternatively you can:

1. Press "Open with GitHub Desktop

   or
3. Press "Download Zip"

## Usage
To use this calculator you input the calculation using the different buttons provided. Then press the equals sign and your result will be displayed

To use the memory function, you can press "M+" to add a number to the memory, "MR" to recall the number saved in the memory and "M" to clear the memory

Buttons such as pi and e will display their values rather than a sign

## Testing
This repository also includes a Unit Test file. To run these tests yourself:

1. Open the calculator.py file
2. Go to the bottom of the code where is shows:
   
![image](https://github.com/user-attachments/assets/384e982e-c069-4891-8bd4-62a12664ddb5)

4. Replace this code with the following:
   if __name__ == "__main__":
    window.mainloop()
   
![image](https://github.com/user-attachments/assets/1c488349-44b5-4ead-9b9e-ba919f1c8d8e)

This is because running the main loop alone does not allow the unit test to take place, therefore you can either delete the code and replace it or you can comment it out to make reverting back to the working calculator much easier

5. Press run on unit_test.py
