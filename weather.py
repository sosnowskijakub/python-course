
temperature = int(input("How high is the temperature outside?\n"))

if temperature > 30 or temperature < -10: 
    print("Stay inside!")
else:
    print("Enjoy the outdoors!")

temperature1 = int(input("How high is the temperature outside?\n"))
forecast = "sunny"

if temperature1 < 30 and forecast != "rainy": 
    print("Go outside!")
else:
    print("Stay inside!")


forecast1 = "rainy"

if not forecast1 == "sunny":
    print("Stay inside!")
else:
    print("Go outside!")


raining = False

if raining:
    print("Stay inside!")
else:
    print("Go outside!")