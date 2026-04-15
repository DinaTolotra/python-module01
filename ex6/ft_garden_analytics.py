class Plant:
    class Statistical:
        def __init__(self) -> None:
            self._age_call_count: int = 0
            self._grow_call_count: int = 0
            self._show_call_count: int = 0

        def increment_age_call_count(self) -> None:
            self._age_call_count += 1

        def increment_grow_call_count(self) -> None:
            self._grow_call_count += 1

        def increment_show_call_count(self) -> None:
            self._show_call_count += 1

        def display(self) -> None:
            print(f"Stats: {self._grow_call_count} grow,",
                  f"{self._age_call_count} age,",
                  f"{self._show_call_count} show")

    def __init__(self, name: str, height: float,
                 age: int) -> None:
        self._name = name
        self.set_height(height, False)
        self.set_age(age, False)
        self.stat: Plant.Statistical = self.Statistical()

    @staticmethod
    def is_year_old(age: int) -> bool:
        return age >= 365

    @classmethod
    def create_anonymous(cls):
        return cls("anonymous", 0., 0)

    def show(self) -> None:
        print(f"{self.get_name().capitalize()}: "
              f"{self.get_height():.1f}cm, "
              f"{self.get_age()} days old")
        self.stat.increment_show_call_count()

    def grow(self, growth_rate: float, day_count: int) -> None:
        self._height += growth_rate * day_count
        self.stat.increment_grow_call_count()

    def age(self, day_count: int) -> None:
        self._age += day_count
        self.stat.increment_age_call_count()

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

    def show(self) -> None:
        super(Flower, self).show()
        print(f" Color: {self.get_color()}")
        if not self._is_blooming:
            print(f" {self._name} has not bloomed yet")
        else:
            print(f" {self._name} is blooming beautifully!")

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


class Tree(Plant):
    class Statistical(Plant.Statistical):
        def __init__(self) -> None:
            super(Tree.Statistical, self).__init__()
            self._shade_call_count: int = 0

        def increment_shade_call_count(self) -> None:
            self._shade_call_count += 1

        def display(self) -> None:
            super(Tree.Statistical, self).display()
            print(f" {self._shade_call_count} shade")

    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super(Tree, self).__init__(name, height, age)
        self.set_trunk_diameter(trunk_diameter, False)
        self._produce_shade: bool = False
        self.stat: Tree.Statistical = self.Statistical()

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
        self.stat.increment_shade_call_count()


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super(Vegetable, self).__init__(name, height, age)
        self.set_harvest_season(harvest_season, False)
        self.set_nutritional_value(0, False)

    def grow(self, growth_rate: float, day_count: int) -> None:
        super(Vegetable, self).grow(growth_rate, day_count)
        nutritional_value: int = self.get_nutritional_value() + day_count
        self.set_nutritional_value(nutritional_value, False)

    def show(self) -> None:
        super(Vegetable, self).show()
        print(" Harvest season:",
              self.get_harvest_season())
        print(" Nutritional value:",
              self.get_nutritional_value())

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
                  "less than 0")
            print("Nutritional value update rejected")

    def get_harvest_season(self) -> str:
        return self._harvest_season

    def get_nutritional_value(self) -> int:
        return self._nutritional_value


class Seed(Flower):
    def __init__(self, name: str, height: float,
                 age: int, color: str) -> None:
        super(Seed, self).__init__(name, height, age, color)

    def set_seed_count(self, seed_count: int,
                       log: bool = True) -> None:
        if seed_count >= 0:
            self._seed_count = seed_count
            if log:
                print("Seed count updated:",
                      self.get_seed_count())
        else:
            print(f"{self.get_seed_count()}:",
                  "Error, seed count can't be",
                  "less than 0")
            print("seed count update rejected")

    def get_seed_count(self) -> int:
        return self._seed_count

    def bloom(self, seed_count: int = 0) -> None:
        super(Seed, self).bloom()
        self.set_seed_count(seed_count, False)


def show_plant_stat(plant: Plant) -> None:
    plant.stat.display()


if __name__ == "__main__":
    rose = Flower("Rose", 15., 10, "red")
    oak = Tree("Oak", 200., 365, 5.)
    tomato = Vegetable("Tomato", 5., 10, "April")
    sunflower = Seed("Sunflower", 80., 45, "yellow")
    anonymous = Plant.create_anonymous()

    print("=== Garden statistics ===")
    print("=== Check year-old")
    print("Is 30 days more than a year? ->", Plant.is_year_old(30))
    print("Is 400 days more than a year? ->", Plant.is_year_old(400))

    print("\n=== Flower")
    rose.show()
    print("[statistics for Rose]")
    show_plant_stat(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(0.8, 10)
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    show_plant_stat(rose)

    print("\n=== Tree")
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.show()
    print("[statistics for oak]")
    show_plant_stat(oak)

    print("\n=== Seed")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(1.5, 20)
    sunflower.age(20)
    sunflower.bloom(42)
    sunflower.show()
    print("[statistics for sunflower]")
    show_plant_stat(sunflower)

    print("\n=== Anonymous")
    anonymous.show()
    print("[statistics for Unknown plant]")
    show_plant_stat(anonymous)
