import doctest
from model.Tank import Tank


class WartechnicManager:

    def __init__(self):
        self.tanks_in_garage = []

    def add_tank_to_garage(self, *tanks_to_add: Tank):
        for tank in tanks_to_add:
            self.tanks_in_garage.append(tank)

    def remove_tank_from_garage(self, *tanks_to_remove: Tank):
        for tank in tanks_to_remove:
            self.tanks_in_garage.remove(tank)

    def find_tanks_by_fuel_consumption(self, fuel_consumption_to_compare: int):

        """
        >>> first_tank = Tank(8, 24.5, 180, 12, 2500, 180)
        >>> second_tank = Tank(4, 17.3, 120, 8, 1500, 270)
        >>> third_tank = Tank(6, 14.3, 140, 6, 3500, 360)

        >>> tank = WartechnicManager()
        >>> tank.add_tank_to_garage(first_tank, second_tank, third_tank)

        >>> result = tank.find_tanks_by_fuel_consumption(20)
        >>> [tank.fuel_consumption for tank in result]
        [17.3, 14.3]
        """

        result: list = []

        for tank in self.tanks_in_garage:
            if tank.fuel_consumption < fuel_consumption_to_compare:
                result.append(tank)
        return result


if __name__ == '__main__':
    doctest.testmod(verbose=False, extraglobs={'tanks_in_garage': WartechnicManager()})
