# CPSC 334 Module 1 (Generative Art)

## Task 1 (Obsolete)
Using Python, this program in `identify.py` creates a black screen. When clicked, a green pixel will appear. Its coordinates will be displayed in stdout, and they will be written in magenta on the screen. If the screen cannot be read (e.g. if the text is cut off), the terminal output should be used. If the terminal output is unreadable while running the program, we suggest exiting the program and reading the value from the terminal when a key point is found, then relaunching the program.

## Task 2
Using Python, this program in `main.py` displays the ETA for the Yale Shuttles ("Yuttle") to arrive at a stop, displayed as pulsing circles on a screen. The program continuously draws circles that fade away slowly, with circle density and movement corresponding to the time that a shuttle is expected to arrive in. Based on how many busses are active, and how far away, you'll see wildly different results. If the screen size is big enough, there will be much more dots to account for it.

![Generative Art](https://youtu.be/d2sUghRlTS0?si=mUJdOdmNxAoiELPD)

### Setup
From within the project directory:
- Create a virtual environment with `python3 -m venv venv `
- Activate the virtual environment with `source venv/bin/activate`
- Install requirements with `pip install -r requirements.txt`
- Run task 2 with `python3 main.py`
- To set up task 2 to run at boot, put this at the end of your `~/.bashrc` file:
    - `sudo python '/home/student334/Desktop/cpsc334-generative-art/main.py'`
- Run task 1 with `python3 identify.py`


### Parameters:
- `STOP_INT`: the stop to monitor (defaults to `10`, representing 333 Cedar)
    - the full list of options is available at https://yale.downtownerapp.com/text/routes. Find the stop then observe the integer at the end of the URL.
- `lifetime`: time (in ms) that circles should remain on the screen (defaults to `20000`)
- `BACKGROUND_COLOR`: the color of the backgroun
- `DEFAULT_COLOR`: the color of the circles that aren't assigned automatically by the bus route
- `NUM_CIRCLES`: the base minimum number of circles before modifications, for each bus
- `NUM_CIRCLES_RANGE`: the possible additional number of circles before modifications, for each bus
- `PULSE_SPEED`: the rate at which circles pusle
- `PULSE_SPEED_RANGE`: the amount which similar circles vary in pusles
- `BASE_PULSE`: pulse size modifier
- `BASE_PULSE_RANGE`: pulse size randomness modifier
- `CIRCLE_SIZE`: circle size modifier
- `CIRCLE_SIZE_RANGE`: circle size randomness modifier
- `CIRCLE_MAX`: maximum pulse size
- `CIRCLE_ADD_RATE`: how frequently to add new circles
- `QUERY_FREQUENCY`: how frequently the bus data is updated
