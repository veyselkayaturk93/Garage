import json

class VehicleRepository:
    @staticmethod
    def read_json():
        # Because there may not be such a file we add an exception checking.
        try:
            with open('vehicles.json') as json_file:
                return json.load(json_file)
        except:
            return []

    @staticmethod
    def write_json(data):
        with open("vehicles.json", "w") as json_file:
            json.dump(data, json_file, indent=2)
