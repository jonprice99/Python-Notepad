# Python Notepad
#### A basic Notepad application built using Python, based on legacy versions of Notepad in Microsoft Windows prior to Windows 11.

## Features
- Create new text files
- Open existing text files
- Save text files
    - Supported file formats: *.txt*, *.docx*, *.pdf*
- Basic text editing
- Insert date and time
- Resizable window
- Basic keyboard shortcuts for easy operation
- Adjustable settings in `config.ini` file
    - Adjustable font, font size, & default window size

## Installation
1. **Clone the repository:** ```git clone https://github.com/jonprice99/python-notepad.git```
2. **Open the Notepad app directory** ```cd python-notepad```
3. **Install dependencies:** This application primarily uses the Tkinter library, which is included with most Python installations. Ensure you have Python installed on your machine.

## Usage
1. **Run the application:** ```python notepad.py```
2. **Create, open, edit, & save text files:** 
    - Use the `File` menu to create, open, or save files
    - Use the `Edit` menu for operations like undo, redo, and time/date insertion

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements
- This project uses the Tkinter library for the graphical user interface.
- This project uses the Pillow module for the app's icon
- Special thanks to the Instructables for their [basic Python text editor tutorial](https://www.instructables.com/Create-a-Simple-Python-Text-Editor/) on which this application is based on.