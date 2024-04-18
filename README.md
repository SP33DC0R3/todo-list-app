# To-Do List Application

## Description
Introducing my first-ever app! As a beginner in python development and still learning the ropes, I'm a bit nervous but excited to share this project with you. Please keep in mind that this app is not at a big production level app, and there might be some bugs or areas that need improvement. However, I've put in a lot of effort to make it functional and user-friendly, and I'm eager to hear your feedback to continue learning and improving. Thank you for trying out my early work in this journey of learning app development!

## About This App
The To-Do List Application is a simple tool for managing tasks and increasing productivity. It allows users to add, edit, complete, and remove tasks from their to-do list.

## How to Run the Application
### Terminal (Linux/Mac/Windows):
1. Ensure Python is installed on your system.
2. Clone or download the source code of the application using `git clone https://github.com/SP33DC0R3/todo-list-app.git`.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the application using `python cli.py`.

### Windows .exe File:
1. Download the provided .exe file.
2. Double-click the .exe file to start the application.

### Webapp:
1. Ensure Python is installed on your system.
2. Clone or download the source code of the application using `git clone https://github.com/SP33DC0R3/todo-list-app.git`.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the application using `streamlit run web.py`.

## Dependencies
- Streamlit
- PySimpleGUI

## Usage Instructions
### For GUI Version:
1. **Adding a New Todo:**
   - Type a new todo in the input box and press Enter or click the "Add" button.
2. **Editing a Todo:**
   - Select a todo from the list and update it in the input box and click the "Edit" button.
3. **Completing a Todo:**
   - Select the todo and click the "Completed" button.
4. **Exiting the Application:**
   - Click the "Exit" button to close the application.

### For CLI Version
1. **Adding a New Todo:**
   - Type "Add" followed by the todo you want to add and then press enter.
2. **Editing a Todo:**
   - Type "Edit" followed by the number of the todo you want to edit and then press enter.
3. **Completing a Todo:**
   - Type "Complete" followed by the number of the todo you have completed and then press enter.
4. **Exiting the Application:**
   - Type "Exit" to exit out of the program.

### For Webapp Version:
1. **Adding a New Todo:**
   - Type a new todo in the input box and press Enter.
2. **Editing a Todo:**
   - Select a todo from the list and update it in the input box.
3. **Completing a Todo:**
   - Check the checkbox next to a todo to mark it as completed.
4. **Exiting the Application:**
   - Close the browser tab and terminal to exit the app.

## Additional Notes and Considerations
- The application stores todos persistently in a text file (`todos.txt`).
- Backup your todo list file regularly to prevent data loss.
- Each instance of the application operates independently with its own todo list.
- Customize the application by modifying the UI, colors, fonts, or adding new features.
