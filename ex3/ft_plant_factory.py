class Plant:
    def __init__(self, name: str, height: float, age_in_day: int) -> None:
        self.name: str = name
        self.height: float = height
        self.age_in_day: int = age_in_day
        print("Created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.height:.1f}cm, "
              f"{self.age_in_day} days old")

    def grow(self, growth_rate: float) -> None:
        self.height += growth_rate

    def age(self) -> None:
        self.age_in_day += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    rose: Plant = Plant("rose", 25, 30)
    oak: Plant = Plant("oak", 200, 365)
    cactus: Plant = Plant("cactus", 5, 90)
    sunflower: Plant = Plant("sunflower", 80, 45)
    fern: Plant = Plant("fern", 15, 120)
