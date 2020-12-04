
def ring(color):
    color = color.lower()
    colors = {
        "schwarz": 0,
        "braun": 1,
        "rot": 2,
        "orange": 3,
        "gelb": 4,
        "grün": 5,
        "blau": 6,
        "lila": 7,
        "grau": 8,
        "weiß": 9
    }
    if not color in colors:

        print("Du hast dich vertippt")
        return False
    return colors[color]


def mult(color):
    color = color.lower()
    colors = {
        "schwarz": 1,
        "braun": 10,
        "rot": 100,
        "orange": 1000,
        "gelb": 10000,
        "grün": 100000,
        "blau": 1000000,
        "lila": 10000000
    }

    if not color in colors:

        print("Du hast dich vertippt")
        return False
    return colors[color]


def tolerance(color):
    color = color.lower()
    colors = {
        "rot": 1.0,
        "braun": 2.0,
        "grün": 0.5,
        "blau": 0.25,
        "lila": 0.1,
        "grau": 0.05,
        "gold": 5,
        "silber": 10
    }
    if not color in colors:

        print("Du hast dich vertippt")
        return False
    return colors[color]


def first_three(one, two, three):
    if two == 0 and three == 0:
        return one
    elif three == 0:
        return 10 * one + two

    else:
        return 100*one + 10*two + three


color = input("Gib die Farbe des ersten Ringes ein:")
ring_one = ring(color)

color = input("Gib die Farbe des zweiten Rings ein:")
ring_two = ring(color)

color = input("Gib deie Farbe des dritten Rings ein:")
ring_three = ring(color)

color = input("Gib die Farbe des vierten Ringes ein:")
ring_four = mult(color)

color = input("Gib die Farbe des fünften Ringes ein:")
ring_five = tolerance(color)


value = first_three(ring_one, ring_two, ring_three)

value = value * ring_four


print(
    f"Der Wert des Widerstandes ist {value} Ohm mit einer Toleranz von {ring_five} Prozent")
