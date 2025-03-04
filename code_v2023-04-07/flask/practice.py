from flask import Flask, request, jsonify

# Create the application instance
app = Flask(__name__)

# send hello json
@app.route("/say", methods=["GET"])

def say_hello():
    json_data = request.json
    # request data should include "message"
    if "message" in json_data:
        return "hello {json_data['message']}"
    # else return 400
    else:
        return "message key is empty", 400


@app.route("/write_line", methods=["POST"])
def write_line():
    # if request contain "line" key
    if "line" in request.json:
    # add a line to "data.txt" and create file if not exists
        with open("data.txt", "a+") as f:
            f.write(request.json["line"] + "\n")
            return "success"
    # else return 400
    else:
        return "line key is empty", 400



app.run("0.0.0.0",81)