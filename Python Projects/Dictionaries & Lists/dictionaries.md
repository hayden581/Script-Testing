# How dictionaries work

A **dictionary** stores pairs of things: a **key** and a **value**.
You use the key to look up the value, just like looking up a word in a real dictionary to find its meaning.

```python
floor = {"Penny Falls": 412.50, "Claw Crane": 236.00, "Pinball": 76.30}
```

| Key           | Value  |
|---------------|--------|
| "Penny Falls" | 412.50 |
| "Claw Crane"  | 236.00 |
| "Pinball"     | 76.30  |

- Curly brackets `{ }` make a dictionary.
- Each pair is written `key: value`, with commas between pairs.
- **Keys must be unique.** You can't have two "Pinball" keys.

---

## Getting a value

Put the key in square brackets:

```python
print(floor["Claw Crane"])      # 236.0
```

With a list you'd need to know the position (`takings[1]`).
With a dictionary you just use the name.

If the key isn't there, Python crashes with a `KeyError`:

```python
print(floor["Lucky Ducks"])     # KeyError: 'Lucky Ducks'
```

---

## Checking a key is there first

Use `in` to check before you use a key:

```python
name = input("Machine: ")
if name in floor:
    print(f"{name} took £{floor[name]:.2f}")
else:
    print(f"{name} is not on the floor.")
```

`in` checks the **keys**, not the values.

---

## Adding and changing values

Setting `floor[key] = value` does one of two things:

- If the key **isn't there**, it **adds** a new pair.
- If the key **is already there**, it **replaces** the old value.

```python
floor["Lucky Ducks"] = 0.0      # new key: adds a machine
floor["Claw Crane"] = 248.50    # existing key: changes the takings
```

To add to a value, read it, then set it again:

```python
floor["Claw Crane"] = floor["Claw Crane"] + 12.50
```

Be careful: because setting a key can overwrite, check with `in` first if you don't want to replace something by accident.

---

## Removing a pair

Use `del` with the key:

```python
del floor["Pinball"]
```

Like getting a value, this crashes if the key isn't there, so check with `in` first.

---

## Looping through a dictionary

A `for` loop over a dictionary gives you each **key**. Use the key to get the value:

```python
total = 0
for name in floor:
    print(f"{name}: £{floor[name]:.2f}")
    total = total + floor[name]
print(f"Total: £{total:.2f}")
```

`len(floor)` tells you how many pairs there are:

```python
print(f"Machines: {len(floor)}")
```

---

## A dictionary inside a dictionary

A value can be anything, even another dictionary.
This lets one key hold **several** pieces of information:

```python
floor = {
    "Penny Falls": {"status": "working",      "takings": 412.50},
    "Air Hockey":  {"status": "out of order", "takings": 54.20},
}
```

Use two sets of square brackets: first the machine, then the detail you want.

```python
print(floor["Air Hockey"]["status"])     # out of order
print(floor["Air Hockey"]["takings"])    # 54.2
```

Adding a new machine means giving it a whole dictionary:

```python
floor["Lucky Ducks"] = {"status": "working", "takings": 0.0}
```

---

## Dictionary vs lists kept in step

With three lists, one machine's details are spread across three places,
held together only by their position:

```python
machines = ["Penny Falls", "Air Hockey"]
takings  = [412.50, 54.20]
status   = ["working", "out of order"]
```

To find Air Hockey you have to search for its position with `index()`, then use that position in the other lists.
If you add or remove a machine in one list but forget another, the lists go out of step and the wrong takings are matched to the wrong machine.

With a dictionary:

- you find a machine straight away by its name
- all of a machine's details stay together under one key
- adding or removing is one line, so nothing goes out of step

---

## Quick reference

| What you want           | Code                          |
|-------------------------|-------------------------------|
| Make a dictionary       | `floor = {"A": 1, "B": 2}`    |
| Get a value             | `floor["A"]`                  |
| Check a key is there    | `if "A" in floor:`            |
| Add or change a value   | `floor["C"] = 3`              |
| Remove a pair           | `del floor["A"]`              |
| Loop through keys       | `for key in floor:`           |
| Count the pairs         | `len(floor)`                  |
| Inner dictionary value  | `floor["A"]["status"]`        |
