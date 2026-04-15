class Plant:
    def __init__(self, name: str,
                 height: float, age: int) -> None:
        self._name = name
        self.set_height(height)
        self.set_age(age)

    def show(self) -> None:
        print(f"{self.get_name().capitalize()}: "
              f"{self.get_height():.1f}cm, "
              f"{self.get_age()} days old")

    def grow(self, growth_rate: float) -> None:
        self._height += growth_rate

    def age(self) -> None:
        self._age += 1

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height: float = height
            print(f"Height updated: {self.get_height()}cm")
        else:
            print(f"{self.get_name()}:",
                  "Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self.get_age()} days")
        else:
            print(f"{self.get_name()}:",
                  "Error, height can't be negative")
            print("Age update rejected")

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> float:
        return self._age


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super(Flower, self).__init__(name, height, age)
        self._is_blooming: bool = False
        self.set_color(color)

    def set_color(self, color: str) -> None:
        if len(color) > 0:
            self._color: str = color
            print("Color updated:",
                  self.get_color())
        else:
            print(f"{self.get_name()}:",
                  "Error, color can't be empty")
            print("Color update rejected")

    def get_color(self) -> str:
        return self._color

    def bloom(self) -> None:
        self._is_blooming = True

    def show(self) -> None:
        super(Flower, self).show()
        print(f" Color: {self.get_color()}\n")
        if self._is_blooming:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super(Tree, self).__init__(name, height, age)
        self.set_trunk_diameter(trunk_diameter)
        self._produce_shade: bool = False

    def set_trunk_diameter(self, trunk_diameter: float) -> None:
        if trunk_diameter > 0:
            self._trunk_diameter: float = trunk_diameter
            print("Trunk diameter updated:",
                  self.get_trunk_diameter())
        else:
            print(f"{self.get_name()}:",
                  "Error, trunk diamater can't",
                  "be negative or eqal to zero")
            print("Trunk diameter update rejected")

    def get_trunk_diameter(self) -> float:
        return self._trunk_diameter

    def produce_shade(self) -> None:
        if not self._produce_shade:
            self._produce_shade = True
        else:
            print(self.get_name(),
                  "produce already shade.")

    def show(self) -> None:
        if self._produce_shade:
            print(self.get_name(),
                  "now produces a shade of",
                  f"{self.get_height()}cm long"
                  f"and {self.get_trunk_diameter()}cm wide.")
        else:
            super(Tree, self).show()

if __name__ == "__main__":
    p = Plant("Plant", 0., 0)
    p.show()
