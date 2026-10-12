table = {
    "Red": "Stop",
    "Yellow": "Slow Down",
    "Green": "Go",
    "Flashing Red": "Stop and Proceed with Caution"
}

def traffic_light_agent(percept):
    return table[percept]

percept_sequence = ["Red", "Green", "Yellow", "Red", "Flashing Red"]

print("Percept\t\tAction")

for color in percept_sequence:
    print(color, "\t", traffic_light_agent(color))