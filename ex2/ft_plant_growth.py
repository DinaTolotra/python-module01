class Plant:
    def __init__(self) -> None:
        self.name: str = ""
        self.height: float = 0
        self.growth_rate: float = 0.
        self.age_in_day: int = 0

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.height:.1f}cm, "
              f"{self.age_in_day} days old")

    def grow(self) -> None:
        self.height += self.growth_rate

    def age(self) -> None:
        self.age_in_day += 1


if __name__ == "__main__":
    rose: Plant = Plant()
    rose_growth: float

    rose.name = "rose"
    rose.height = 25.
    rose.growth_rate = 0.8
    rose.age_in_day = 30
    rose_growth = rose.height
    print("=== Garden Plant Growth ===")
    for day in range(1, 7 + 1):
        print(f"=== Day {day} ===")
        rose.show()
        rose.grow()
        rose.age()
    rose_growth = rose.height - rose_growth
    print(f"Growth this week: {round(rose_growth)}cm")
