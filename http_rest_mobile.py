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

		if(id == "lastbooking"):
			parser = reqparse.RequestParser()
			parser.add_argument("id")
			parser.add_argument("tid")
			parser.add_argument("cid")
			parser.add_argument("cc")
			parser.add_argument("ow")
			parser.add_argument("cr")
			parser.add_argument("fk")
			parser.add_argument("date")
			parser.add_argument("valid")
			parser.add_argument("gpsco")
			parser.add_argument("addInfo")
			parser.add_argument("base64jpg")
			args = parser.parse_args()

			for station in stations:
				if(id == station["id"]):
					station["tid"] = args["tid"]
					station["cid"] = args["cid"]
					station["cc"] = args["cc"]
					station["ow"] = args["ow"]
					station["cr"] = args["cr"]
					station["fk"] = args["fk"]
					station["date"] = args["date"]
					station["valid"] = args["valid"]
					station["gpsco"] = args["gpsco"]
					station["addInfo"] = args["addInfo"]
					station["base64jpg"] = "".join(args["base64jpg"].split())			
					#print('update: ', station)
					return station, 200

		if(id == "lastgps"):
			parser = reqparse.RequestParser()
			parser.add_argument("id")
			parser.add_argument("tid")
			parser.add_argument("date")
			parser.add_argument("co")
			args = parser.parse_args()

			for station in stations:
				if(id == station["id"]):
					station["tid"] = args["tid"]
					station["date"] = args["date"]
					station["co"] = args["co"]
					#print('update: ', station)
					return station, 200
	

	def put(self, id):
		if(id == "bookings"):
			count = 0
			for path in pathlib.Path(id).iterdir():
				if path.is_file():
					count += 1
			for station in stations:
				if(id == station["id"]):
					amount_received = station["amount_received"]
					amount_received += 1
					if(count == amount_received):
						station["same_number_of_files"] = True
					if(count != amount_received):
						station["same_number_of_files"] = False
					station["amount_folder"] = count
					station["amount_received"] = amount_received

			parser = reqparse.RequestParser()
			parser.add_argument("id")
			parser.add_argument("tid")
			parser.add_argument("cid")
			parser.add_argument("cc")
			parser.add_argument("ow")
			parser.add_argument("cr")
			parser.add_argument("fk")
			parser.add_argument("date")
			parser.add_argument("valid")
			parser.add_argument("gpsco")
			parser.add_argument("addInfo")
			parser.add_argument("base64jpg")
			args = parser.parse_args()
		
			stationToJson = {
				#"id" : id,
				"tid": args["tid"],
				"cid" : args["cid"],
				"cc" : args["cc"],
				"ow" : args["ow"],
				"cr" : args["cr"],
				"fk" : args["fk"],
				"date" : args["date"],
				"valid" : args["valid"],
				"gpsco" : args["gpsco"],
				"addInfo" : args["addInfo"],
				"base64jpg" : "".join(args["base64jpg"].split())
			}

			filename = ((args["date"].replace('-','')).replace(' ','_')).replace(':','') + ".json"
			#station["gpsco"].replace('\u00b0', 'stopien')
			with open(args["id"]+"/"+filename, 'w', encoding='utf8') as outfile:
				json.dump(stationToJson, outfile, ensure_ascii=False)


			stations.append(station)
			return station, 201
		
		if(id == "gps"):

			count = 0
			for path in pathlib.Path(id).iterdir():
				if path.is_file():
					count += 1
			for station in stations:
				if(id == station["id"]):
					amount_received = station["amount_received"]
					amount_received += 1
					if(count == amount_received):
						station["same_number_of_files"] = True
					if(count != amount_received):
						station["same_number_of_files"] = False
					station["amount_folder"] = count
					station["amount_received"] = amount_received

			parser = reqparse.RequestParser()
			parser.add_argument("id")
			parser.add_argument("tid")
			parser.add_argument("date")
			parser.add_argument("co")
			args = parser.parse_args()
		
			stationToJson = {
				#"id" : id,
				"tid": args["tid"],
				"date" : args["date"],
				"co" : args["co"]
			}

			filename = ((args["date"].replace('-','')).replace(' ','_')).replace(':','') + ".json"
			#station["co"].replace('\u00b0', 'stopien')
			with open(args["id"]+"/"+filename, 'w', encoding='utf8') as outfile:
				json.dump(stationToJson, outfile, ensure_ascii=False)

			stations.append(station)
			return station, 201

		if(id == "bookings" or id == "gps"):
			count = 0
			for path in pathlib.Path(id).iterdir():
				if path.is_file():
					count += 1
			for station in stations:
				if(id == station["id"]):
					amount_received = station["amount_received"]
					amount_received += 1
					if(count == amount_received):
						station["same_number_of_files"] = True
					if(count != amount_received):
						station["same_number_of_files"] = False
					station["amount_folder"] = count
					station["amount_received"] = amount_received
			return station, 201
	

api.add_resource(Station, "/<id>")

app.run(debug=True, host= '0.0.0.0')
