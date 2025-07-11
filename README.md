# ProSensia Python Internship – Weekly Progress

This file documents my daily work and learnings during the Python internship at ProSensia using the Scrimba platform.

## Day 01  
I learned how to use the Brython environment to run Python in the browser, how to work with variables, data types, and how to convert between them using typecasting. 
-> In today’s task, I made a program that took an integer, a float, and a string from the user, stored them in separate variables, and printed them using formatted output.

## Day 02  
I learned how to slice strings, take user input, and perform arithmetic operations in Python. 
-> In today’s task, I built a simple program that took a full name as input, sliced out the first and last name, then took two numbers and performed addition, subtraction, multiplication, and division, displaying all results nicely.

## Day 03  
I learned how to work with lists, split and join strings, and use tuples to store data that shouldn't change.
-> In today’s task, I wrote a program that took a sentence, split it into a list of words, joined them back with dashes, and stored my first and last name in a tuple, accessing each part using indexing.

## Day 04  
I learned how sets are used to store unique items, how tuples are immutable, and how to write clean code using comments.
-> For today’s task, I created a basic student record system that stored student IDs in a tuple, managed course names using a set (adding and removing courses), and included inline comments to explain the logic.

## Day 05  
I learned how to define and use functions in Python, including passing parameters, using default values, and calling functions with named arguments.
-> In today’s task, I made a GPA calculator program that takes a list of grades, calculates the average using a function, and returns the GPA rounded to two decimal places. I used a formatted print statement to display the result clearly.


## Day 06  
I learned how to use Boolean logic and comparison operators along with if, elif, and else statements to control program flow.
-> In today’s task, I created a conditional grading system that takes a numeric score, validates it, and then maps it to a letter grade using conditionals. I also added a second function that prints a formatted grade summary using named parameters like "Student Zara scored 87.5 → Grade: A-".


## Day 07  
I learned how to work with for loops, while loops, and nested loops, and how to use the enumerate() function to track index values.
-> In today’s task, I created a smart list analyzer program that manually sorted a list of numbers without using any built-in functions. I used loops to calculate the sum, average, minimum, and maximum of the list, returned the results in a dictionary, and printed them using a second function with a loop and enumerate(). I also handled user input and added input validation.


## Day 08  
I learned how to use dictionaries to build a contact book, store nested information, and access data using keys. 
-> In today’s task, I made a dynamic contact book that lets users add, update, retrieve, and view all contacts using a while loop menu system. I validated emails, prevented duplicate entries, normalized names using   .title(), and used dictionary operations to handle all features in a beginner-friendly way.


## Day 09  
I learned how to read and process text files with `open()` and the `with` context manager, and how to write robust code using `try`, `except`, and `finally` blocks. 
-> In today’s task, I built a student‑marks reader that prompts for a file path, reads each line, cleans and validates the data, skips entries with missing or invalid marks, stores valid results in a dictionary, prints each student’s mark, and safely calculates the class average while counting how many records were skipped.


## Day 10  
I learned how to define classes, constructors, and use inheritance in Python to build organized, modular programs.
-> In today’s task, I built an inventory management system using object-oriented programming. I created a base class for products and a subclass for perishable items that apply discounts if expiry is near. I also created an inventory manager class to add, search, and list products, and used lambda functions and comprehensions to filter and export data. I moved the restock logic to a separate file and imported it using a utility module.

[ 📁 On GitHub, I organized this by keeping the main program file in the `Week-3/Day-10/` folder and placed the helper module `inventory_utils.py` in the same directory to keep the code clean and modular.]

## Day 11  
I learned how to build a full employee management system using object-oriented programming, file handling, and modular code design. 
-> In today’s task, I created a program that can store, search, sort, and report employee data from a text file. I made separate classes for `Employee` and `EmployeeManager`, used lambda functions for filtering, and handled errors using try-except blocks. The code is split into multiple files for better organization, and a report is generated in a separate file based on the stored data.

[📁 For more details, visit the **Day-11.Dir** folder in the repository and read the `readme.md` file there.]

