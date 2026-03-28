class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        if height < 0:
            height = 0.
        if age < 0:
            age = 0
        self._name: str = name
        self._height: float = height
        self._age: int = age
        print("Plant created: ", end="")
        self.show()

    def show(self) -> None:
        print(f"{self._name.capitalize()}: "
              f"{self._height:.1f}cm, "
              f"{self._age} days old")

    def grow(self, growth_rate: float) -> None:
        self._height += growth_rate

    def age(self) -> None:
        self._age += 1

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
            print(f"Height updated: {self.get_height()}cm")
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
            print(f"Age updated: {self.get_age()} days")
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> float:
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose: Plant = Plant("rose", 15., 10)
    print("")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-42)
    rose.set_age(-84)
    print("\nCurrent state: ", end="")
    rose.show()
