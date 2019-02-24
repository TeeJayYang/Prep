"""
There is a queue of cars waiting at a gas stations.
There are 3 full dispensers at the station, labeled X,Y,Z
respectively. Each dispenser has some finite amount of
fuel, and the amount of available fuel is clearly displayed
on each dispenser.

When a car arrives at the front of the queue, the driver
can choose to drive to any dispenser not occupied by
another car. Suppose that the fuel demand is D litres for
this car. The driver must choose a dispenser that has at
least D liters of fuel. If all unoccupied dispensers have
less than D liters, the dirver must wait for some other
car to finish tanking up. If all dispensers are unoccupied,
and none has at least D liters, the driver is unable to
refuel the car and it blocks the queue indefinitely. If
more than one unoccupied dispenser has at least D liters,
the driver chooses the one labeled with the smallest letter
among them.

Each driver will have to wait some amount of time before he
or she starts refueling the car. Calculate the maximum
waiting time among all drivers. Assuming that tanking one
liter of fuel takes exactly one second, and moving cars
is instantaneous.

Example:
    Input: 
        A = [ 2, 8, 4, 3, 2 ]
        X = 7
        Y = 11
        Z = 3
    Output:
        8
"""

def MaxWaitingTime(A, X, Y, Z):
    # A is the queue of cars of size within range [1,100000]
    # each element in A is within range[1, 1 billion]
    # X,Y,Z are the gas stations with capacity within range [1, 1 billion]
    dispensers = [X, Y, Z]
    cars = [0]*3
    total = 0

    def enterCar(c):
        candidate = None
        candidate_car = max(cars)
        for i in reversed(range(3)):
            if dispensers[i] >= c and cars[i] <= candidate_car:
                candidate = i
                candidate_car = cars[i]
        if candidate is None:
            return -1
        time = cars[candidate]
        dispensers[candidate] -= c
        for i in range(3):
            cars[i] = max(cars[i]-time, 0)
        cars[candidate] = c
        return time

    for c in A:
        time = enterCar(c)
        if time == -1:
            return -1
        else:
            total += time
        # print (cars, dispensers, c, time)
    return total
