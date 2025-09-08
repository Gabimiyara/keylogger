from iWriter import IWriter
from flask import jsonify
import requests



class WriteServer(IWriter):
    def __init__(self):
        self.url = "http://127.0.0.1:5000/save_data"
    def send_data(self, data, machine_name):
        data = {machine_name:data}
        requests.post(self.url,json=data)


a = WriteServer()
a.send_data("this","is work")