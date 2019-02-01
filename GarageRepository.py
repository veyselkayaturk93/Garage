import json


class GarageRepository:
    @staticmethod
    def read_json():
        with open('garage.json') as json_file:
            return json.load(json_file)

    @staticmethod
    def write_json(data):
        with open("garage.json", "w") as json_file:
            json.dump(data, json_file, indent=2)
