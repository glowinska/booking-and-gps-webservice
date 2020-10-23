#!/usr/bin/env python

from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
import pathlib

app = Flask(__name__)
api = Api(app)

def base64jpg():
	x = """/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAoHBwgHBgoICAgLCgoLDhgQDg0NDh0VFhEYIx8lJCIf
	IiEmKzcvJik0KSEiMEExNDk7Pj4+JS5ESUM8SDc9Pjv/2wBDAQoLCw4NDhwQEBw7KCIoOzs7Ozs7
	0jfUuox21NdIZUzjcDIppSd3FQIQU1+Cv//Z"""
	return "".join(x.split())



stations = [
	{ 'id' : 'lastbooking', 'tid': '', 'cid' : '', 'cc' : '', 'ow' : '', 'cr' : '', 'fk' : '', 'date' : '', 'valid' : '', 'gpsco' : '' ,'addInfo' : '', 'base64jpg' : '' }, 
	{ 'id' : 'bookings', 'amount_received' : 0 , 'amount_folder' : 0 , 'same_number_of_files' : True },
	{ 'id' : 'gps', 'amount_received' : 0 , 'amount_folder' : 0 , 'same_number_of_files' : True },
	{ 'id' : 'lastgps', 'tid': '', 'date' : '', 'co' : '' }
]

def count():
	count = 0
	for path in pathlib.Path(id).iterdir():
		if path.is_file():
			count += 1
	return count

class Station(Resource):
	def get(self, id):
		for station in stations:
			if("{}".format(id) == station["id"]):
				if(id == "bookings" or id == "gps"):
					count = 0
					for path in pathlib.Path(id).iterdir():
						if path.is_file():
							count += 1
					station["amount_folder"] = count
					if(station["amount_folder"] == station["amount_received"]):
						station["same_number_of_files"] = True
					else:
						station["same_number_of_files"] = False
				return station, 200
		return "Station {} not found".format(id), 404
	
	def post(self, id):
		return station, 201
	
	def put(self, id):
		return station, 201
	

api.add_resource(Station, "/<id>")

app.run(debug=True, host= '0.0.0.0')
