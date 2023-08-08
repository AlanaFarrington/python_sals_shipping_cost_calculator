weight = 41.5
cost = 0
drone_cost = 0
print("Item weight: " + str(weight) + "lbs")

#Ground shipping
if weight <= 2:
  cost = 20 + (weight * 1.50)
elif weight > 2 and weight <= 6:
  cost = 20 + (weight * 3.00)
elif weight > 6 and weight <= 10:
  cost = 20 + (weight * 4.00)
else:
  cost = 20 + (weight * 4.75)
print("Ground shipping cost will be $" + str(cost))

#Ground shipping Premium
premium_cost = 125.00
print("Ground shipping premium cost will be $" + str(premium_cost))

#Drone shipping
if weight <= 2:
  drone_cost = weight * 4.50
elif weight > 2 and weight <= 6:
  drone_cost = weight * 9.00
elif weight > 6 and weight <= 10:
  drone_cost = weight * 12.00
else:
  drone_cost = weight * 14.25
print("Ground shipping cost will be $" + str(drone_cost))