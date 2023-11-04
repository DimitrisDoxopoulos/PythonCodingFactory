from collections import deque

# create a deque
garage = deque()

# simulate some cars arriving in the garage
garage.append("car 1")
garage.append("car 2")
garage.append("car 3")
garage.append("car 4")
garage.append("car 5")

# Simulate a car leaving the garage (FIFO)
car_left = garage.popleft()
# print(car_left)

# Simulate some cars arriving in the garage
garage.append("car 7")
garage.append("car 8")

print("Current status of the garage: ", list(garage))
print("Last car which left from garage: ", car_left)
