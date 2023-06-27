# add the jsonify method to your Flask import
from flask import Flask, jsonify, request
app = Flask(__name__)

# suppose you have your data in the variable named some_data
todos = [
   { "label": "My first task", "done": False }
]

@app.route('/', methods=['GET'])
def hello_world():
    # you can convert that variable into a json string like this
    json_text = jsonify(todos)

    # and then you can return it to the front end in the response body like this
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'




@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    #removes it at that position
    todos.remove(position)
    # returns the string version
    return jsonify(todos)



# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)