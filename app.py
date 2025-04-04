from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/generate", methods=["GET"])
def generate_timetable():
    timetable = "Here is your timetable!"  # Replace with your function
    return jsonify({"timetable": timetable})

if __name__ == "__main__":
    app.run(debug=True)
