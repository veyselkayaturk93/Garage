from GarageService import GarageService
from VehicleService import VehicleService

# TO DO  create texts on ViewHandler class and throw exception here.
class ViewPresenter:

    @staticmethod
    def add_vehicle(brand, model, license_plate, year):
        if not GarageService.is_there_available_garage():
            return "Error: No available garage"
        if VehicleService.is_license_plate_exists(license_plate):
            return "Error: The vehicle which you want to park is already in garage."
        garage = GarageService.add_vehicle_and_update_availability()
        VehicleService.add_vehicle(brand, model, license_plate, year, garage)
        return "Location of {} {} {} is {}.".format(brand, model, license_plate, garage)

    @staticmethod
    def remove_vehicle(license_plate):
        if not VehicleService.is_license_plate_exists(license_plate):
            return "Error: The vehicle which you want to remove from garage is not exist."
        vehicle = VehicleService.remove_vehicle(license_plate)
        GarageService.remove_vehicle_and_update_availability(vehicle['garage'])
        return "{} {} {} is removed from {}.".format(vehicle['brand'], vehicle['model'], vehicle['id'], vehicle['garage'])

    @staticmethod
    def get_availabilities():
        availabilities = GarageService.get_availabilities()
        text = "Board "
        for garage in availabilities.keys():
            text += "{}: {} ".format(garage, availabilities[garage])
        return text
