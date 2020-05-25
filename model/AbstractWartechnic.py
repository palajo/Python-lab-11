class AbstractWartechnic:

    def __init__(self, engine_volume: int, fuel_consumption: float, max_speed: float, passengers_capacity: int,
                 fire_range: int):
        self.engine_volume = engine_volume
        self.fuel_consumption = fuel_consumption
        self.max_speed = max_speed
        self.passengers_capacity = passengers_capacity
        self.fire_range = fire_range
