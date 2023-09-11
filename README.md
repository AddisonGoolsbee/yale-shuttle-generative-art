## CPSC 334 Module 1
# Generative Art
Using Python, this program creates a black screen. When clicked, a green pixel will appear. Its coordinates will be displayed in stdout, and they will be written in magenta on the screen. If the screen cannot be read (e.g. if the text is cut off), the terminal output should be used. If the terminal output is unreadable while running the program, we suggest exiting the program and reading the value from the terminal when a key point is found, then relaunching the program.

### Setup
From within the project directory:
- Create a virtual environment with `python3 -m venv venv `
- Activate the virtual environment with `source venv/bin/activate`
- Install requirements with `pip install -r requirements.txt`
- Run the script with `python3 main.py`