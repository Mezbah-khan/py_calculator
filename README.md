# py_calculator
Project Overview
This project demonstrates how to create a basic calculator web application using Flask for the backend, HTML for the frontend, and CSS for styling. Users can input mathematical expressions, which the server evaluates and returns the result.

Project Structure
The project consists of the following key files:

app.py: The main Flask application that handles routing, processing the mathematical expression, and rendering the HTML template.
templates/index.html: The HTML template that defines the structure of the webpage (input field for calculations, result display).
static/style.css: The CSS file used to style the webpage and make the calculator visually appealing.
Steps:
Flask Setup:

The Flask app is initialized in app.py, which handles both GET and POST requests.
On POST, the calculator evaluates the mathematical expression input by the user using Python's eval() function and returns the result.
HTML Template (index.html):

An input field is provided for the user to type in a mathematical expression.
The form is submitted using the POST method, which sends the input to the server for processing.
The result of the calculation is displayed below the form.
Styling (style.css):

The page is styled with a clean and simple design.
The layout is made responsive, with centered content and clean fonts, improving user experience on both desktop and mobile devices.
How to Run:
Install Flask by running pip install flask.
Create the necessary files (app.py, index.html, and style.css) as shown in the directory structure.
Run the Flask app using python app.py.
Open a browser and go to http://127.0.0.1:5000/ to use the calculator.
Key Features:
Simple Input: Users can enter a mathematical expression.
Real-time Calculation: After pressing "Calculate", the result is shown without page reloads.
Clean UI: The calculator is styled with CSS to provide a user-friendly experience.
This project serves as a basic introduction to web development with Flask and provides a foundation for creating more complex web applications.











