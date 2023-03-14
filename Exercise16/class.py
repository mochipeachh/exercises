# person, employee and customer
class Person:
    def __init__(self, name: str, eye_colour: str, favourite_animal: str):
        if not name:
            raise ValueError("Missing name")
        if eye_colour.title() not in ["Brown", "Green", "Blue"]:
            raise ValueError("Invalid eye_colour")
        self.name = name
        self.eye_colour = eye_colour
        self.favourite_animal = favourite_animal

    def __str__(self):
        return f"{self.name} has {self.eye_colour} eyes"

    def conjure_animal(self):
        match self.favourite_animal:
            case "cat":
                return "🐱"
            case "dog":
                return "🐶"
            case "frog":
                return "🐸"
            case "turtle":
                return "🐢"
            case "duck":
                return "🦆"
            case "rabbit":
                return "🐰"
            case _:
                return "❔"


def main():
    banana = get_person()
    print(banana)
    print("and viola ! your favourite animal has been conjured")
    print(banana.conjure_animal())


def get_person():
    name = input("Name: ")
    eye_colour = input("Eye colour: ")
    favourite_animal = input("Favourite animal: ")
    return Person(name, eye_colour, favourite_animal)


if __name__ == "__main__":
    main()
