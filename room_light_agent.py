def room_light_agent(percept):
    if percept == "Dark":
        return "Turn Light ON"
    elif percept == "Bright":
        return "Turn Light OFF"
    elif percept == "Dim":
        return "Leave Light As Is"
    else:
        return "Invalid Percept"

percept_sequence = ["Dark", "Dim", "Bright", "Dark"]

print("Percept\tAction")

for percept in percept_sequence:
    action = room_light_agent(percept)
    print(f"{percept}\t{action}")
