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


## Day 12  
I built a simple client interpreter program in Python that reads a text file sent by a client and extracts useful information like the project name, list of features, timeline, and priority. The program then prints a clean summary on the screen and saves it to a new `.txt` file. As a bonus, it also creates a `.json` file where each feature is marked as "Not Started" to help track progress later. It's basically like a mini assistant that reads a client’s project brief and turns it into a clear and usable summary.

[📁 For more details, check the **Day-12** folder and read the `readme.md` file there.]


## Day 13  
I created a Python program that connects to a public currency exchange API and fetches live exchange rates for selected currencies. I used the ExchangeRate API (`https://api.exchangerate-api.com/v4/latest/USD`) to get the latest data in JSON format. The program extracts useful details like the base currency, date, and rates for specific currencies such as EUR, GBP, PKR, INR, and more. It then prints a neat summary on the screen and saves the results to a text file named `exchange_report.txt`.


## Day 14  
I worked on visualizing data using Python libraries like Matplotlib, Seaborn, and Pandas. I loaded and cleaned sales data from a CSV file and then created multiple charts: a line chart to show monthly revenue for Product A, a bar chart for product revenue in March, a pie chart to show market share distribution, and a correlation heatmap for product revenue comparison. All plots were saved to the `/plots` folder as image files.


## Day 15  
I built a simple desktop app with a graphical user interface using `customtkinter` that allows users to encrypt and decrypt text. The app takes user input, processes it through basic encryption/decryption logic, and displays an encyypted format message in a clean and responsive GUI.

[📁 For more details, check the **Day-15** folder and read the `readme.md` file there.]


## Day 16  
I created a simple command-line notes app using Python's `argparse` module and `colorama` for colorful terminal output. The app allows users to add, view, and delete notes, which are all saved to a `notes.txt` file.

[📁 For more details, check the **Day-16** folder and read the `readme.md` file there.]


## Day 17
I learned how to write unit tests using Python’s unittest module and how to log errors using the logging module.
-> In today’s task, I updated the Day-13 currency script by adding try-except blocks, logging important events to error_log.txt, and creating a test_script.py file with unit tests for key functions. The code is now more reliable, testable, and production-ready.

[📁 For more details, check the Day-17 folder and read the readme.md file there.]


## Day 18  
I built an automated CSV/Excel report generator that loads structured sales data, calculates revenue per product, identifies the top-performing item, and generates a summary report in text format. It also displays a bar chart of product-wise revenue using Matplotlib.

[📁 For more details, check the **Day-18** folder and read the `readme.md` file there.]


## Day 19
I was tasked with deploying an encryption tool I had previously built using CustomTkinter. Since GUI apps can't be directly hosted online, I rebuilt the app using Streamlit and deployed it on Streamlit Cloud to make it publicly accessible via a web link.

[📁 The actual deployment was done in a separate repo
🔗 GitHub: zain-the-npc/VaultCode]


## Day 20  
I built an advanced typing speed test app in Python with difficulty levels, live stats, and colorful terminal output using `colorama`.

[📁 For more details, check the **Day-20** folder and read the `readme.md` file there.]


## Day 21  
I created a weather web app called *Mausam* using Streamlit. It fetches real-time weather data from an API and presents it in a clean, user-friendly UI with dynamic styling and visuals.

[📁 For more details, check the **Day-21** folder and read the `readme.md` file there.]


## Day 22  
I built a GUI-based Typing Speed Test using Streamlit. The app lets users select difficulty, type the passage, and then calculates WPM, accuracy, and errors in a clean, interactive interface.

[📁 For more details, check the **Day-22** folder and read the `readme.md` file there.]


## Day 23  
I focused on portfolio polishing. This included updating my GitHub profile README, organizing pinned repositories, enhancing my LinkedIn profile with internship details, and writing a self-reflection on my progress throughout the internship.

[📁 For more details, check the **Day-23** folder and read the `readme.md` file there.]


## Day 24  
I finalized and submitted my internship capstone project — TypeRush, a fully functional typing speed test web app built with Streamlit. All required features were completed, the code was structured into modules, and full documentation with screenshots and deployment link was added.

[📁 For more details, check the **Day-24** folder and read the `readme.md` file there.]


## Day 25  
Today was Capstone Demo Day! We were asked to present our final project, reflect on our learning journey, and share our experience with others. I summarized the key features of my capstone, discussed what I built, how it works, and what I learned throughout the internship.

[📁 For more details, check the **Day-25** folder and read the `readme.md` file there.]


## Day 26  
I built a simple Fuzzy Q&A Bot in Python that answers predefined fun questions without using any external API. It uses fuzzy string matching to handle typos and slight wording changes, ensuring the bot responds even when input isn’t an exact match.  

[📁 For more details, check the **Day-26** folder and read the `readme.md` file there.]


## Day 27  
I created a simple ReAct Agent demo that follows the Reason + Act framework for AI agents. The bot simulates thought steps, chooses actions, observes results, and produces a final answer. For this demo, the LLM is mocked, and the only tool implemented is a basic calculator.

[📁 For more details, check the **Day-27** folder and read the `readme.md` file there.]


## Day 28  
I extended my previous ReAct Agent demo to include command parsing and function execution. Instead of relying on a mocked LLM, the agent now directly reads plain text commands, determines the corresponding function, executes it with the right arguments, and returns the result. The Thought → Action → Observation → Final Answer flow remains the same, but now supports multiple tools such as add, subtract, and greet.

[📁 For more details, check the **Day-28** folder and read the `readme.md` file there.]

