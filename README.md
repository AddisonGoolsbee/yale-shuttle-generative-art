# CPSC 334 Module 1 (Generative Art)

[![Video Demo](https://youtu.be/d2sUghRlTS0?si=mUJdOdmNxAoiELPD](https://www.youtube.com/watch?v=YOUR_VIDEO_ID_HERE)

## Task 1
Using Python, this program in `identify.py` creates a black screen. When clicked, a green pixel will appear. Its coordinates will be displayed in stdout, and they will be written in magenta on the screen. If the screen cannot be read (e.g. if the text is cut off), the terminal output should be used. If the terminal output is unreadable while running the program, we suggest exiting the program and reading the value from the terminal when a key point is found, then relaunching the program.

### Setup
From within the project directory:
- Create a virtual environment with `python3 -m venv venv `
- Activate the virtual environment with `source venv/bin/activate`
- Install requirements with `pip install -r requirements.txt`
- Run the script with `python3 identify.py`

## Task 2
Using Python, this program in `main.py` displays the ETA for the Yale Shuttle ("Yuttle") to arrive at a stop. The program continuously draws circles that fade away slowly, with circle density (or size) corresponding to the time that a shuttle is expected to arrive in.

### Setup
From within the project directory:
- Create a virtual environment with `python3 -m venv venv `
- Activate the virtual environment with `source venv/bin/activate`
- Install requirements with `pip install -r requirements.txt`
- Run the script with `python3 identify.py`


### Parameters:
`stop_int`: the stop to monitor (defaults to `10`, representing 333 Cedar)
- the full list of options is available at https://yale.downtownerapp.com/text/routes. Find the stop then observe the integer at the end of the URL.

`lifespan`: time (in ms) that circles should remain on the screen (defaults to `20000`)
