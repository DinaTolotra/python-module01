class Plant:
    def __init__(self, name: str,
                 height: float, age: int) -> None:
        self._name = name
        self.set_height(height, False)
        self.set_age(age, False)

    def show(self) -> None:
        print(f"{self.get_name().capitalize()}: "
              f"{self.get_height():.1f}cm, "
              f"{self.get_age()} days old")

    def grow(self, growth_rate: float) -> None:
        self._height += growth_rate

    def age(self) -> None:
        self._age += 1

    def set_height(self, height: float, log: bool = True) -> None:
        if height >= 0:
            self._height: float = height
            if log:
                print(f"Height updated: {self.get_height()}cm")
        else:
            print(f"{self.get_name()}:",
                  "Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int, log: bool = True) -> None:
        if age >= 0:
            self._age = age
            if log:
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
        self.set_color(color, False)

    def set_color(self, color: str, log: bool = True) -> None:
        if len(color) > 0:
            self._color: str = color
            if log:
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
        print(f" Color: {self.get_color()}")
        if not self._is_blooming:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super(Tree, self).__init__(name, height, age)
        self.set_trunk_diameter(trunk_diameter, False)
        self._produce_shade: bool = False

    def set_trunk_diameter(self, trunk_diameter: float,
                           log: bool = True) -> None:
        if trunk_diameter > 0:
            self._trunk_diameter: float = trunk_diameter
            if log:
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
                  "already producing shade.")

    def show(self) -> None:
        if self._produce_shade:
            print(self.get_name(),
                  "now produces a shade of",
                  f"{self.get_height()}cm long"
                  f"and {self.get_trunk_diameter()}cm wide.")
        else:
            super(Tree, self).show()
            print(" Trunk diameter:",
                  self.get_trunk_diameter())


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.set_harvest_season(harvest_season, False)
        self.set_nutritional_value(0, False)

    def set_harvest_season(self, harvest_season: str,
                           log: bool = True) -> None:
        if harvest_season:
            self._harvest_season = harvest_season
            if log:
                print("Harvest season updated:",
                      self.get_harvest_season())
        else:
            print(f"{self.get_name()}:",
                  "Error, harvest season can't be empty")
            print("Harvest season update rejected")

    def set_nutritional_value(self, nutritional_value: int,
                              log: bool = True) -> None:
        if nutritional_value >= 0:
            self._nutritional_value = nutritional_value
            if log:
                print("Nutritional value updated:",
                      self.get_nutritional_value())
        else:
            print(f"{self.get_name()}:",
                  "Error, nutritional value can't be",
                  "less or equal to 0")
            print("Nutritional value update rejected")

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    def grow(self, growth_rate: float) -> None:
        super(Vegetable, self).grow(growth_rate)
        nutritional_value: int = self.get_nutritional_value() + 1
        self.set_nutritional_value(nutritional_value, False)

    def show(self) -> None:
        super(Vegetable, self).show()
        print(" Harvest season:",
              self.get_harvest_season())
        print(" Nutritional value:",
              self.get_nutritional_value())


if __name__ == "__main__":
    rose = Flower("Rose", 15., 10, "red")
    oak = Tree("Oak", 200., 365, 5.)
    tomato = Vegetable("Tomato", 5., 10, "April")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show()

    print("\n=== Vegetable")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow(2.1)
        tomato.age()
    tomato.show()
