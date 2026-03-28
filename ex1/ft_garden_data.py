class Plant:
    def __init__(self) -> None:
        self.name: str = ""
        self.height: int = 0
        self.age: int = 0

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.height}cm, "
              f"{self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    rose: Plant = Plant()
    rose.name = "rose"
    rose.height = 25
    rose.age = 30
    rose.show()
