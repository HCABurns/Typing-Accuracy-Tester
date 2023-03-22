# Typing speed tester

This is a project to determine the typing speed and accuracy of a user. A UI will be created using the Tkinter and phrases will be retrieved from a database using SQL. Additonally, this program has been threaded for one thread to deal with the UI and the other for input processing.

## What is the purpose of this project?

This project has been created to create a program to test and experiment with the Tkinter package for creating a UI. Additionally, I want to consolidate my knowledge of threading in python so will be adding this functionality.

## Project Extension:

After completing the main goal of this project, I have decided to extend the scope by adding in a score metric. Additionally, a server will be created to allow for retreiving and updating a global database. To go along with this, another scene will need to be created to display the scores and allow for searching and filtering the results.

## To do list:

 * Create a unittesting file that will be used to test functions to ensure they're working correctly.
 * Provide a score (accuracy * wpm * 1/len(phrase)?)
 * Have a leaderboard section to show the top _ scores.
 * Store scores in database (Relational with what phrase it was achieved with - for filtering)
 * Server and client to retrieve and update scores.
