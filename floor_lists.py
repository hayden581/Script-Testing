# Arcade Floor - Part 1: the floor in lists

machines = ["Penny Falls", "Claw Crane", "Air Hockey", "Racing Car",
            "Basketball", "Dance Mat", "Space Shooter", "Pinball"]
takings = [412.50, 236.00, 54.20, 187.40, 98.60, 31.80, 145.00, 76.30]
status = ["working", "working", "out of order", "working",
          "working", "out of order", "working", "working"]


def show_floor():
    total = 0
    for i in range(len(machines)):
        print(f"{machines[i]}: £{takings[i]:.2f}")
        total = total + takings[i]
    print(f"Total: £{total:.2f}")


def add_machine():
    name = input("New machine: ").strip()
    while name == "" or name in machines:
        if name == "":
            print("Please type a name.")
        else:
            print(f"{name} is already on the floor.")
        name = input("New machine: ").strip()
    # keep all three lists in step
    machines.append(name)
    takings.append(0.0)
    status.append("working")
    print(f"{name} has joined: {len(machines)} machines")


def remove_machine():
    name = input("Machine leaving: ").strip()
    if name in machines:
        i = machines.index(name)
        # remove from every list at the same position
        machines.pop(i)
        takings.pop(i)
        status.pop(i)
        print(f"{name} has left the floor.")
        show_floor()
    else:
        print(f"{name} is not on the floor.")


def best_and_worst():
    best = 0
    worst = 0
    for i in range(1, len(machines)):
        if takings[i] > takings[best]:
            best = i
        if takings[i] < takings[worst]:
            worst = i
    print(f"Best earner: {machines[best]} (£{takings[best]:.2f})")
    print(f"Worst earner: {machines[worst]} (£{takings[worst]:.2f})")


def working_total():
    total = 0
    for i in range(len(machines)):
        if status[i] == "working":
            total = total + takings[i]
    print(f"Working machines took: £{total:.2f}")


# CORE
show_floor()
add_machine()

# SECURE
remove_machine()

# STRETCH
best_and_worst()
working_total()
