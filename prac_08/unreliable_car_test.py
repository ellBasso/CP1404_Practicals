from prac_08.unreliable_car import UnreliableCar

bomb = UnreliableCar("Bomb", 100, 30)
print(f"The bad car drive {bomb.drive(20)}km")

corolla = UnreliableCar("Beast", 100, 100)
print(f"The Corolla drove {corolla.drive(100)}km")
