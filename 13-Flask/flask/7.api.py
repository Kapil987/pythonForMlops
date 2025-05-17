### Put and Delete-HTTP Verbs
### Working With API's--Json
## Create a TO-DO list in json

from flask import Flask, jsonify, request

app = Flask(__name__)

##Initial Data in my to do list, The below Data can come from a DB like mongodb
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "Welcome To The Sample To DO List App"

## Get: Retrieve all the items

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## get: Retireve a specific item by Id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id): # 1
    for item in items:
        if item["id"] == item_id: # 1 or as 2 or else
            return jsonify(item)
    return jsonify({"error": "item not found"})

# ## Post :create a new task- API
# @app.route('/items',methods=['POST'])
# def create_item():
#     if not request.json or not 'name' in request.json:
#         return jsonify({"error":"item not found"})
#     new_item={
#         "id": items[-1]["id"] + 1 if items else 1,
#         "name":request.json['name'],
#         "description":request.json["description"]


#     }
#     items.append(new_item)
#     return jsonify(new_item)

# # Put: Update an existing item
# @app.route('/items/<int:item_id>',methods=['PUT'])
# def update_item(item_id):
#     item_to_update = None
#     for item in items:
#         if item["id"] == item_id:
#             item_to_update = item
#             break  # Exit the loop once the item is found

#     if item_to_update is None:
#         return jsonify({"error": "Item not found"})

#     item_to_update['name'] = request.json.get('name', item_to_update['name'])
#     item_to_update['description'] = request.json.get('description', item_to_update['description'])
#     return jsonify(item_to_update)

# # DELETE: Delete an item
# @app.route('/items/<int:item_id>', methods=['DELETE'])
# def delete_item(item_id):
#     global items
#     items = [item for item in items if item["id"] != item_id]
#     return jsonify({"result": "Item deleted"})


if __name__ == '__main__':
    app.run(debug=True)
