from flask import Flask, request, jsonify

# Create the application instance
app = Flask(__name__)

friends = [
{
    "answers": [
        {
            "quiz_id": "1",
            "option": "option1"
        },
        {
            "quiz_id": "2",
            "option": "option2"
        },
        {
            "quiz_id": "3",
            "option": "option2"
        }
    ]
}
]

@app.route("/friends/get", methods=["GET"])
def get_friends():
    return jsonify(friends)

@app.route("/friends/get/<int:friend_num>", methods=["GET"])
def get_friend(friend_num):
    return jsonify(friends[friend_num])

@app.route("/friends/add", methods=["POST"])
def add_friend():
    json_data = request.json

    return f"success added friend [{json_data['friend']['name']}]"

app.run("0.0.0.0",81)