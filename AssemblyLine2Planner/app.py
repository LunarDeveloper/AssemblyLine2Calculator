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

# Flask route in app.py
@app.route('/calculate', methods=['POST'])
def calculate():
    item_name = request.json.get('item_name')
    quantity = int(request.json.get('quantity'))

    if item_name in items:
        item = items[item_name]
        if item.recipe:
            from anytree import Node, RenderTree

            # Create the root node and build the crafting tree
            root = Node(f"{quantity}x {item_name}")
            item.recipe.build_tree(quantity, root)

            # Convert the tree into JSON-like format for the frontend
            nodes = []
            edges = []
            node_index = {}

            def traverse(node, parent_id=None, index=0):
                node_id = len(nodes)
                nodes.append({"id": node_id, "label": node.name})
                node_index[node] = node_id
                if parent_id is not None:
                    edges.append({"from": parent_id, "to": node_id})

                for child in node.children:
                    traverse(child, node_id)

            traverse(root)

            return jsonify({"nodes": nodes, "edges": edges})
        else:
            return jsonify({'error': 'Item is a base resource and does not have a recipe.'})
    else:
        return jsonify({'error': 'Item not found.'})


if __name__ == '__main__':
    app.run(debug=True)
