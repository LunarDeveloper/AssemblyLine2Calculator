import json

# Class Definitions
class Item:
    def __init__(self, name):
        self.name = name
        self.recipe = None

    def set_recipe(self, recipe):
        self.recipe = recipe

    def __str__(self):
        return self.name

class Recipe:
    def __init__(self, output_item, items, craft_machine):
        self.output_item = output_item
        self.items = items  # Dictionary {item: quantity}
        self.craft_machine = craft_machine

    def calculate_resources(self, quantity):
        total_requirements = {}

        for item, qty in self.items.items():
            required_qty = qty * quantity

            # Check if the item has a recipe, if not, it's a base resource
            if item.recipe:
                sub_requirements = item.recipe.calculate_resources(required_qty)
                for sub_item, sub_qty in sub_requirements.items():
                    if sub_item in total_requirements:
                        total_requirements[sub_item] += sub_qty
                    else:
                        total_requirements[sub_item] = sub_qty
            else:
                # Base resource, add it directly
                if item in total_requirements:
                    total_requirements[item] += required_qty
                else:
                    total_requirements[item] = required_qty

        return total_requirements

class Machine:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
    def __str__(self):
        return f"{self.name} (speed: {self.speed})"

# Load JSON data from the files
with open("./data/resources.json", "r") as resources_file:
    resources_data = json.load(resources_file)

with open("./data/machines.json", "r") as machines_file:
    machines_data = json.load(machines_file)

# Dictionaries to store instances of Items and Machines
items = {}
machines = {}

# Step 2: Create Item and Machine Instances
# Create items
for item_name in resources_data:
    items[item_name] = Item(item_name)

# Create machines
for machine_name, machine_data in machines_data.items():
    machines[machine_name] = Machine(machine_name, machine_data["speed"])

# Step 3: Set up Recipes for Items
for item_name, recipe_data in resources_data.items():
    item = items[item_name]
    required_items = {items[sub_item]: qty for sub_item, qty in recipe_data["items"].items()}
    machine_name = recipe_data["craft"]
    craft_machine = machines[machine_name]

    recipe = Recipe(item, required_items, craft_machine)
    item.set_recipe(recipe)

# Example Usage to Calculate Resources for 1 "ai_robot"
def print_resources(item_name, quantity):
    if item_name in items:
        item = items[item_name]
        if item.recipe:
            required_resources = item.recipe.calculate_resources(quantity)
            print(f"Resources required to craft {quantity}x {item_name}:")
            for item, qty in required_resources.items():
                print(f"- {qty}x {item.name}")
        else:
            print(f"Item '{item_name}' does not have a recipe and is a base resource.")
    else:
        print(f"Item '{item_name}' not found.")


# Calculate resources needed to craft 1 AI Robot
print_resources("ai_robot", 1)