Week 3 Assignment on Conditions and Loops
Description
Grade Reporter & Bug Hunt

Put this week's two big ideas - repeating work with loops and making decisions with conditions - to work in two small programs.

This assignment will help you practice:

Looping through a list with for
Choosing between several outcomes with if / elif / else
Building up a running total or count inside a loop
Reading a while loop and understanding when it stops
Finding a bug that produces no error message at all

Files to create (use these exact names):

grade_reporter.py
bug_hunt.py

GitHub repository name to use (public, exact): plp-python-week3

Your submission for this assignment is one link: your public GitHub repository containing all the files above. Use these exact file and repository names so your submission matches the marking checklist.
    Part A - Grade Reporter

Create the file grade_reporter.py.

Start your file with this list. Do not change these numbers.

scores = [72, 45, 90, 61, 38]

Use a for loop to go through every score in the list.
Inside the loop, use if / elif / else to work out a grade: 80 and above is A, 70 to 79 is B, 50 to 69 is C, and below 50 is F.
Print each score with its grade on its own line.
Count how many learners passed (a score of 50 or more) and print the number that passed and the number that failed.
Add up all the scores and print the average, rounded to one decimal place round(average, 1).

Every number you print must be worked out by your code. Do not count the passes yourself and type in 3.

Required results:

A working grade_reporter.py that prints a grade for all five scores.
The pass count, the fail count, and the average, all calculated by your program.