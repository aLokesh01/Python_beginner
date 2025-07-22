
weather = "rainy"
if weather == "sunny":
    print("wear sunglass")
elif weather == "rainy":
    print("carry an umbrella")
else:
    print("check the weather forecast")


weather_day = "monday"
match weather_day:

    case "monday":
        pass
    case "friday":
        pass
    case _:
        pass


def greet():
    return "hello!"

def farewell():
    return "goodbye!"

def unknown():
    return "unknown action"

# Dictionary-based switch
action = "greet"
switch_dict = {
    "greet": greet,
    "bye": farewell
}


print(switch_dict.get(action, unknown)())
