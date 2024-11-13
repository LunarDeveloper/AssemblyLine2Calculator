from flask import Flask, render_template, request, jsonify
import json
from classes import items  # Assuming you've already set up items and recipes

app = Flask(__name__)

# Load JSON data
with open('./data/resources.json', 'r') as resources_file:
    resources_data = json.load(resources_file)
with open('./data/machines.json', 'r') as machines_file:
    machines_data = json.load(machines_file)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint to get crafting tree
@app.route('/calculate', methods=['POST'])
def calculate():
    item_name = request.form.get('item_name')
    quantity = int(request.form.get('quantity'))

    if item_name in items:
        item = items[item_name]
        if item.recipe:
            from anytree import Node, RenderTree

            # Create the root node and build the crafting tree
            root = Node(f"{quantity}x {item_name}")
            item.recipe.build_tree(quantity, root)

            # Render the tree as a string to be displayed
            tree_output = ""
            for pre, _, node in RenderTree(root):
                tree_output += f"{pre}{node.name}\n"

            return jsonify({'tree': tree_output})
        else:
            return jsonify({'error': 'Item is a base resource and does not have a recipe.'})
    else:
        return jsonify({'error': 'Item not found.'})

if __name__ == '__main__':
    app.run(debug=True)
