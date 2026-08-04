# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Please enter the package weight in kilograms: "))
rate = float(input("Please enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} GBP")

