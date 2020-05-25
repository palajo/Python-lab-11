from model.AbstractWartechnic import AbstractWartechnic


class Artillery(AbstractWartechnic):

    def __init__(self, engine_volume: int, fuel_consumption: float, max_speed: float, passengers_capacity: int,
                 fire_range: int, rocket_quantity: int):
        super(Artillery, self).__init__(engine_volume, fuel_consumption, max_speed, passengers_capacity, fire_range)

        self.rocket_quantity = rocket_quantity

    def __str__(self, engine_volume: int, fuel_consumption, max_speed, passengers_capacity,
                fire_range, rocket_quantity):
        return \
            "Engine volume: " + str(engine_volume) + "\n" \
            "Fuel consumption: " + str(fuel_consumption) + "\n" \
            "Max. speed: " + str(max_speed) + "\n" + \
            "Passengers capacity: " + str(passengers_capacity) + "\n" + \
            "Fire range: " + str(fire_range) + "\n" + \
            "Rockets quantity: " + str(rocket_quantity) + "\n"
