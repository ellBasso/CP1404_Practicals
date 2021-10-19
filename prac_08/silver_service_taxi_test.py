"""Test the new SilverServiceTaxi class"""

from prac_08.silver_service_taxi import SilverServiceTaxi

snazzy = SilverServiceTaxi("Snazzy", 100, 12)
print(snazzy)
snazzy.drive(10)
print(snazzy)
print(f"The fare is ${snazzy.get_fare():.2f}")

test = SilverServiceTaxi("Test", 100, 2)
test.drive(18)
print(f"The fare for the {test.current_fare_distance}km trip is ${test.get_fare():.2f}")
