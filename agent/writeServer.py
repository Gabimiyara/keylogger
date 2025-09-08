from iWriter import IWriter
from flack import jsonify
import requests
import os
from helper_function import get_hostname



class WriteServer(IWriter):
    def __init__(self):
        self.url = "http://127.0.0.1:5000/save_data"
    def send_data(self, data):
        machine_name = get_hostname()
        data = {machine_name:data}
        requests.post(self.url,json=data)


a = WriteServer()
a.send_data("I am ")