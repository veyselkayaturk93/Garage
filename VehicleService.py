from VehicleRepository import VehicleRepository


class VehicleService:
    
    @staticmethod
    def is_license_plate_exists(license_plate):
        data = VehicleRepository.read_json()
        for vehicle in data:
            if vehicle["id"] == license_plate:
                return True
        return False

    @staticmethod
    def add_vehicle(brand, model, license_plate, year, garage):
        data = VehicleRepository.read_json()
        vehicle = {'id': license_plate, 'brand': brand, 'model': model, 'year': year, 'garage': garage}
        data.append(vehicle)
        VehicleRepository.write_json(data)
    
    @staticmethod
    def remove_vehicle(license_plate):
        data = VehicleRepository.read_json()
        for vehicle in data:
            if vehicle["id"] == license_plate:
                data.remove(vehicle)
                VehicleRepository.write_json(data)
                return vehicle
