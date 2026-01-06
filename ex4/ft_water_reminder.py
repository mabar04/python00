def ft_water_reminder():
    waterdays = int (input("Days since last watering: "))
    if waterdays >= 2 :
        print("Water the plants!")
    else:
        print("Plants are fine")
