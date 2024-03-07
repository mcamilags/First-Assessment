class Inventory:
    def __init__(self):
        self.resources = {
            "computers": 10,
            "bicycles": 20
        }

    def update_inventory(self, resource, quantity):
        if resource in self.resources:
            self.resources[resource] += quantity
        else:
            self.resources[resource] = quantity
        return f"Inventory updated. {resource}: {self.resources[resource]}"

    def display_inventory(self):
        print("Inventory:")
        for resource, quantity in self.resources.items():
            print(f"{resource}: {quantity}")
