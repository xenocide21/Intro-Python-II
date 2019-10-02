class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"Player has picked up {self.name}.\n---")

    def on_drop(self):
        print(f"Player has dropped {self.name}.\n---")