temp=float(input("Enter the temperature in degree Celsius (*C) :"))
if temp<=10:
    print("It's a cold Temperature")
elif temp>10 and temp<=25:
    print("It's a Normal Temperature")
elif temp>25:
    print("It's a Hot Temperature")

fahrenheit = (temp * 9/5) + 32

print(f"{temp}°C is equal to {fahrenheit}°F")