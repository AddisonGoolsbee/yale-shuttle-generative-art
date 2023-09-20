import pygame
import sys
import math
import random
import requests

# Constants
BACKGROUND_COLOR = (0, 0, 0)
DEFAULT_COLOR = (255, 0, 0)
NUM_CIRCLES = 10
NUM_CIRCLES_RANGE = 5
PULSE_SPEED = 0.2
PULSE_SPEED_RANGE = 0.5
BASE_PULSE = 0.2
BASE_PULSE_RANGE = 0.4
CIRCLE_SIZE = 2
CIRCLE_SIZE_RANGE = 3
CIRCLE_MAX = 20


# Name, circles, and time away for each bus route
class Bus:
    def __init__(self, name, current_time=30, color=DEFAULT_COLOR):
        self.name = name
        self.circles = []
        self.current_time = current_time
        self.modifier = (1 / current_time) * 30
        self.color = color

    def __str__(self):
        return f"Name: {self.name}, Circles: {self.circles}, Current Time: {self.current_time}"

    def getCircles(self):
        for _ in range(
            int(
                random.uniform(NUM_CIRCLES, NUM_CIRCLES_RANGE + NUM_CIRCLES)
                * self.modifier
            )
        ):
            circle_radius = (
                random.randint(CIRCLE_SIZE, CIRCLE_SIZE_RANGE + CIRCLE_SIZE)
                * self.modifier
            )
            circle_max_radius = (
                random.randint(CIRCLE_MAX, CIRCLE_MAX + CIRCLE_SIZE_RANGE)
                * self.modifier
            )
            circle_pulse_speed = (
                random.uniform(PULSE_SPEED, PULSE_SPEED + PULSE_SPEED_RANGE)
                * self.modifier
            )
            circle_position = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
            pulsing_factor = (
                random.uniform(BASE_PULSE, BASE_PULSE + BASE_PULSE_RANGE)
                * self.modifier
            )
            self.circles.append(
                (
                    circle_radius,
                    circle_max_radius,
                    circle_pulse_speed,
                    circle_position,
                    pulsing_factor,
                )
            )


stop_int = 10
# Fetch JSON data
url = f"https://yale.downtownerapp.com/routes_eta.php?stop={stop_int}"
response = requests.get(url)
data = response.json()

# Extract shuttle details
shuttle_details = data["etas"][f"{stop_int}"]["etas"]

# Group results by route and find the closest shuttle for each route
closest_shuttles = {}
for detail in shuttle_details:
    route = detail["route"]
    # If the route isn't in closest_shuttles yet, or the new detail has an earlier arrival time, update it.
    if route not in closest_shuttles or detail["avg"] < closest_shuttles[route]["eta"]:
        closest_shuttles[route] = {"eta": detail["avg"]}
# print to stdout for debugging (and fun!)
print(closest_shuttles)


# gets the eta for a given route_int
def get_eta(route_int):
    return closest_shuttles[route_int]["eta"]


# gets the color associated with a given route_int
def route_to_color(route_int):
    # keep a dictionary of route_int to an RGB color
    route_to_color_dict = {
        1: (33, 100, 255),  # weekday blue
        2: (255, 165, 0),  # weekday orange
        3: (255, 20, 20),  # weekday red
        4: (138, 212, 255),  # weekend daytime blue
        5: (255, 187, 135),  # Orange - Weekday Daytime Express
        6: (148, 255, 194),  # Grocery
        7: (158, 87, 0),  # Cedar
        8: (255, 30, 230),  # Pink - VA
        9: (0, 255, 102),  # Green
        10: (185, 115, 255),  # Purple - Weekend Express
        11: (100, 50, 0),  # Brown
        12: (255, 255, 0),  # Yellow
        13: (28, 28, 255),  # Blue Night
        14: (201, 151, 0),  # Orange Night
    }
    # return the color for the route
    return route_to_color_dict[route_int]


# Initialize Pygame
pygame.init()

# Get the screen size
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h

if pygame.display.Info().current_w > 1000:
   NUM_CIRCLES *= 3


# Create the fullscreen screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Pulsing Circles")

# list of all currently active busses
busses = [
    Bus("Orange", color=(255, 165, 0)),
    Bus("Blue", color=(0, 0, 255)),
    Bus("Cedar", color=(0, 255, 0)),
]

for bus in busses:
    bus.getCircles()

print(len(busses[0].circles), len(busses[1].circles))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    for bus in busses:
        for circle_props in bus.circles:
            (
                circle_radius,
                circle_max_radius,
                circle_pulse_speed,
                circle_position,
                pulsing_factor,
            ) = circle_props

            pulse_radius = circle_radius + (
                circle_max_radius - circle_radius
            ) * pulsing_factor * (
                1 + math.sin(pygame.time.get_ticks() / 1000 * circle_pulse_speed)
            )
            pygame.draw.circle(screen, bus.color, circle_position, int(pulse_radius))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
