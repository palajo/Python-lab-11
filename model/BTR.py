import AbstractWartechnic


class BTR(AbstractWartechnic):

    def __init__(self, engine_volume: int, fuel_consumption: float, max_speed: float, passengers_capacity: int,
                 fire_range: int, wheels_quantity: int, trunk_capacity: int):

        super(BTR, self).__init__(engine_volume, fuel_consumption, max_speed, passengers_capacity, fire_range)

        self.wheels_quantity = wheels_quantity
        self.trunk_capacity = trunk_capacity

    def __str__(self, engine_volume: int, fuel_consumption, max_speed, passengers_capacity,
                fire_range, wheels_quantity, trunk_capacity):
        return \
            "Engine volume: " + str(engine_volume) + "\n" \
            "Fuel consumption: " + str(fuel_consumption) + "\n" \
            "Max. speed: " + str(max_speed) + "\n" + \
            "Passengers capacity: " + str(passengers_capacity) + "\n" + \
            "Fire range: " + str(fire_range) + "\n" + \
            "Wheels quantity: " + str(wheels_quantity) + "\n" + \
            "Trunk capacity: " + str(trunk_capacity) + "\n"
