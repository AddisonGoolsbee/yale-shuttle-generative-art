import requests

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
        closest_shuttles[route] = {
            "eta": detail["avg"]
        }
# print to stdout for debugging (and fun!)
print(closest_shuttles)

def get_eta(route_int):
    return closest_shuttles[route_int]["eta"]

def route_to_color(route_int):
    # keep a dictionary of route_int to an RGB color
    route_to_color_dict = {
        1: (33, 100, 255), # weekday blue
        2: (255, 165, 0), # weekday orange
        3: (255, 20, 20), # weekday red
        4: (138, 212, 255), # weekend daytime blue
        5: (255, 187, 135), # Orange - Weekday Daytime Express
        6: (148, 255, 194), # Grocery
        7: (158, 87, 0), # Cedar
        8: (255, 30, 230), # Pink - VA
        9: (0, 255, 102), # Green
        10: (185, 115, 255), # Purple - Weekend Express
        11: (100, 50, 0), # Brown
        12: (255, 255, 0), # Yellow
        13: (28, 28, 255), # Blue Night
        14: (201, 151, 0), # Orange Night
    }
    # return the color for the route
    return route_to_color_dict[route_int]
