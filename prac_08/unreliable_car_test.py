from prac_08.unreliable_car import UnreliableCar

corolla = UnreliableCar("Beast", 100, 100)

bomb = UnreliableCar("Bomb", 100, 30)
for i in range(1, 20):
    """Both cars should only drive 100km due to range constraints.
    The bomb shouldn't drive every time."""
    print(f"The Corolla drove {corolla.drive(100)}km")
    print(f"The bad car drive {bomb.drive(20)}km")
    print(bomb)
    print(corolla)
