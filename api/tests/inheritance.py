class Parent:
    def greet(self):
        return "hello from parent"


class Child(Parent):
    def __init__(self, title) -> None:
        super().__init__()
        self.title = title

    def greet(self):
        print(super().greet())
        print(f"the given title is: {self.title}")
        return "hello from child"


c = Child("Survey Monkey")
print(c.greet())
