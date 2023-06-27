# Import necessary modules from flask
from flask import Flask, jsonify, request

# Create a new Flask web server
app = Flask(__name__)

# Initialize a list of todos
todos = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
]


# Define the route for the URL "/todos" to get all todos
@app.route('/todos', methods=['GET'])
def get_todos():
    # Convert the todos list into JSON and return it as a response
    return jsonify(todos)



# Define the route for the URL "/todos" to add a new todo
@app.route('/todos', methods=['POST'])
def add_new_todo():
    # Append a new todo at the end of the todos list
    todos.append({
        "done": False,  # The new todo is not done yet
        "label": "Sample Todo " + str(len(todos) + 1)  # The label of the new todo
    })
    # Convert the updated todos list into JSON and return it as a response
    return jsonify(todos)



# Define the route for the URL "/todos/<position>" to delete a todo at a specific position
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # Check if the position is within the range of the todos list
    if position < len(todos):
        # If it is, remove the todo at that position
        todos.pop(position)
        # Convert the updated todos list into JSON and return it as a response
        return jsonify(todos)

# Run the Flask web server if this file is the main program
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
