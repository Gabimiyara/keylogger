from flask import Flask, jsonify, request
import os
import json
from helper_function_server import stamp_date,stamp_time

app = Flask(__name__)

@app.route('/save_data',methods=['POST'])
def receive():
    data = request.get_json()


    file_name = "data.json"
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        logs = {}
    else:
        with open(file_name, "r") as file:
            logs = json.load(file)


    key = list(data)[0]
    date = stamp_date()
    time = stamp_time()

    if not key in logs:
        logs[key] = {date:None}
    if not date in logs[key]:
        logs[key][date] = {time:None}
    logs[key][date][time] = data[key]

    with open(file_name, "w") as file:
        json.dump(logs, file, indent=4)

    return jsonify({"status": "success", "data": data}), 200

        



if __name__== "__main__":
    app.run(debug=True)