from GarageRepository import GarageRepository


class GarageService:
    @staticmethod
    def __find_most_available_garage_index(data):
        availability = 0
        index = -1
        i = 0
        for garage in data:
            if garage["availability"] > availability:
                availability = garage["availability"]
                index = i
            i += 1
        return index

    @staticmethod
    def is_there_available_garage():
        data = GarageRepository.read_json()
        for garage in data:
            if garage["availability"] > 0:
                return True
        return False

    @staticmethod
    def get_availabilities():
        data = GarageRepository.read_json()
        availabilities = {}
        for garage in data:
            availabilities[garage["name"]] = garage["availability"]
        return availabilities

    @staticmethod
    def add_vehicle_and_update_availability():
        data = GarageRepository.read_json()
        i = GarageService.__find_most_available_garage_index(data)
        if i >= 0:
            data[i]["availability"] -= 1
            GarageRepository.write_json(data)
            return data[i]["name"]
        return None

    @staticmethod
    def remove_vehicle_and_update_availability(garage_name):
        data = GarageRepository.read_json()
        for garage in data:
            if garage['name'] == garage_name:
                garage["availability"] += 1
                GarageRepository.write_json(data)
                break
