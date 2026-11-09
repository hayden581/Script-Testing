# Arcade Floor - Part 2: the floor as a dictionary
# STRETCH version: each machine's value is its own dictionary

floor = {
    "Penny Falls":   {"status": "working",      "takings": 412.50},
    "Claw Crane":    {"status": "working",      "takings": 236.00},
    "Air Hockey":    {"status": "out of order", "takings": 54.20},
    "Racing Car":    {"status": "working",      "takings": 187.40},
    "Basketball":    {"status": "working",      "takings": 98.60},
    "Dance Mat":     {"status": "out of order", "takings": 31.80},
    "Space Shooter": {"status": "working",      "takings": 145.00},
    "Pinball":       {"status": "working",      "takings": 76.30},
}


def ask_amount(prompt):
    # keeps asking until a number of 0 or more is typed
    while True:
        text = input(prompt).replace("£", "").strip()
        try:
            amount = float(text)
            if amount >= 0:
                return amount
            print("The amount cannot be negative.")
        except ValueError:
            print("Please type a number, like 12.50")


def add_takings():
    name = input("Machine: ").strip()
    while name not in floor:
        print(f"{name} is not on the floor.")
        name = input("Machine: ").strip()
    print(f"{name} took £{floor[name]['takings']:.2f}")
    extra = ask_amount("Taken since: £")
    floor[name]["takings"] = floor[name]["takings"] + extra
    print(f"{name} now: £{floor[name]['takings']:.2f}")


def add_machine():
    name = input("New machine: ").strip()
    while name == "" or name in floor:
        if name == "":
            print("Please type a name.")
        else:
            print(f"{name} is already on the floor.")
        name = input("New machine: ").strip()
    floor[name] = {"status": "working", "takings": 0.0}
    print(f"{name} has joined: {len(floor)} machines")


def remove_machine():
    name = input("Machine leaving: ").strip()
    while name not in floor:
        print(f"{name} is not on the floor.")
        name = input("Machine leaving: ").strip()
    del floor[name]
    print(f"{name} has left: {len(floor)} machines")


def closing_report():
    print()
    print("--- Closing report ---")
    working = 0
    for name in floor:
        machine = floor[name]
        print(f"{name} | {machine['status']} | £{machine['takings']:.2f}")
        if machine["status"] == "working":
            working = working + machine["takings"]
    print(f"Working machines took: £{working:.2f}")


print(f"Machines: {len(floor)}")

# CORE
add_takings()

# SECURE
add_machine()
remove_machine()

# STRETCH
closing_report()
