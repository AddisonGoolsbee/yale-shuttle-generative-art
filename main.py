import pygame
import sys
import math
import random
import requests

# Constants
BACKGROUND_COLOR = (0, 0, 0)
DEFAULT_COLOR = (255, 0, 0)
NUM_CIRCLES = 50
NUM_CIRCLES_RANGE = 15
PULSE_SPEED = 1
PULSE_SPEED_RANGE = 0.5
BASE_PULSE = 1
BASE_PULSE_RANGE = 3
CIRCLE_SIZE = 4
CIRCLE_SIZE_RANGE = 3
CIRCLE_MAX = 12
# Integer representing the stop we want to display data for
STOP_INT = 2
# Out of 255, how transparent should the circles be?
TRANSPARENCY = 128


# Name, circles, and time away for each bus route
class Bus:
    def __init__(self, name, current_time=30, color=DEFAULT_COLOR):
        self.name = name
        self.circles = []
        self.current_time = current_time
        self.modifier = self.calculate_modifier()
        self.color = color

    def __str__(self):
        return f"Name: {self.name}, Circles: {self.circles}, Current Time: {self.current_time}"

    def __lt__(self, other):
        return self.current_time > other.current_time

    def calculate_modifier(self):
        a = (self.current_time) / 5
        b = max(3 - a, 1)
        return b

    def getCircles(self):
        # Adjust the base number of circles based on ETA.
        base_circles = int(60 / (self.current_time + 1))
        for _ in range(
            int(
                random.uniform(NUM_CIRCLES, NUM_CIRCLES_RANGE + NUM_CIRCLES)
                * self.modifier
            )
        ):
            circle_radius = random.uniform(
                CIRCLE_SIZE, CIRCLE_SIZE_RANGE + CIRCLE_SIZE
            ) * (self.modifier**1.5)
            circle_max_radius = random.uniform(
                CIRCLE_MAX, CIRCLE_MAX + CIRCLE_SIZE_RANGE
            ) * (self.modifier**1.3)
            circle_pulse_speed = random.uniform(
                PULSE_SPEED, PULSE_SPEED + PULSE_SPEED_RANGE
            ) * (self.modifier**1.5)
            circle_position = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
            pulsing_factor = (
                random.uniform(BASE_PULSE, BASE_PULSE + BASE_PULSE_RANGE)
                * self.modifier
                / 5
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


# Fetch JSON data
url = f"https://yale.downtownerapp.com/routes_eta.php?stop={STOP_INT}"
response = requests.get(url)
data = response.json()

# Extract shuttle details
shuttle_details = data["etas"][f"{STOP_INT}"]["etas"]


# gets the eta for a given route_int
def get_eta(route_int):
    return closest_shuttles[route_int]["eta"]


# gets the color associated with a given route_int
def route_to_color(route_int):
    # keep a dictionary of route_int to an RGB color
    route_to_color_dict = {
        1: (33, 100, 255, TRANSPARENCY),  # weekday blue
        2: (255, 165, 0, TRANSPARENCY),  # weekday orange
        3: (255, 20, 20, TRANSPARENCY),  # weekday red
        4: (138, 212, 255, TRANSPARENCY),  # weekend daytime blue
        5: (255, 187, 135, TRANSPARENCY),  # Orange - Weekday Daytime Express
        6: (148, 255, 194, TRANSPARENCY),  # Grocery
        7: (158, 87, 0, TRANSPARENCY),  # Cedar
        8: (255, 30, 230, TRANSPARENCY),  # Pink - VA
        9: (0, 255, 102, TRANSPARENCY),  # Green
        10: (185, 115, 255, TRANSPARENCY),  # Purple - Weekend Express
        11: (100, 50, 0, TRANSPARENCY),  # Brown
        12: (255, 255, 0, TRANSPARENCY),  # Yellow
        13: (28, 28, 255, TRANSPARENCY),  # Blue Night
        14: (201, 151, 0, TRANSPARENCY),  # Orange Night
    }
    # return the color for the route
    return route_to_color_dict[route_int]


# Group results by route and find the closest shuttle for each route
closest_shuttles = {}
for detail in shuttle_details:
    route = detail["route"]
    # If the route isn't in closest_shuttles yet, or the new detail has an earlier arrival time, update it.
    if route not in closest_shuttles or detail["avg"] < closest_shuttles[route]["eta"]:
        closest_shuttles[route] = {"eta": detail["avg"], "color": route_to_color(route)}
# print to stdout for debugging (and fun!)
print(closest_shuttles)

# Initialize Pygame
pygame.init()

# Get the screen size
screen_info = pygame.display.Info()
WIDTH, HEIGHT = screen_info.current_w, screen_info.current_h

if pygame.display.Info().current_w > 2500:
    NUM_CIRCLES *= 3


# Create the fullscreen screen
pygame.display.set_mode().convert_alpha()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Pulsing Circles")

# list of all currently active busses
busses = []
for route, details in closest_shuttles.items():
    bus_name = f"Bus {route}"
    bus_color = details["color"]
    bus_eta = details["eta"]
    bus = Bus(bus_name, current_time=bus_eta, color=bus_color)
    busses.append(bus)

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

    for bus in sorted(busses):
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
            temp_surface = pygame.Surface(
                (2 * int(pulse_radius), 2 * int(pulse_radius)), pygame.SRCALPHA
            )
            pygame.draw.circle(
                temp_surface,
                bus.color,
                (int(pulse_radius), int(pulse_radius)),
                int(pulse_radius),
            )
            screen.blit(
                temp_surface,
                (
                    circle_position[0] - int(pulse_radius),
                    circle_position[1] - int(pulse_radius),
                ),
            )

    pygame.display.flip()
    clock.tick(120)

pygame.quit()
sys.exit()
