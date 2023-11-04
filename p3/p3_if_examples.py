def clothing_recommendation_elif(temperature):
    if temperature < 32:
        return "It's very cold!\nYou should wear a coat, hat, gloves, and a scarf."
    elif temperature < 50:
        return "It's cold!\nYou should wear a coat, hat, and gloves."
    elif temperature < 60:
        return "It's cool!\nA light jacket, hat, and gloves would be a good choice."
    elif temperature < 90:
        return "Wear shorts"
    else:
        return "It's not too cold.\nYou may not need a coat, but a hat and gloves can still be useful."






def clothing_recommendation_nested(temperature):

    if temperature < 32:
        return "It's very cold!\nYou should wear a coat, hat, gloves, and a scarf."
    else:
        if temperature < 50:
            return "It's cold!\nYou should wear a coat, hat, and gloves."
        else:
            if temperature < 60:
                return "It's cool!\nA light jacket, hat, and gloves would be a good choice."
            else:
                return "It's not too cold.\nYou may not need a coat, but a hat and gloves can still be useful."






def main():
    temperature = float(input("Enter the temperature in degrees Fahrenheit: "))

    # Using the first function with elif statements
    recommendation_if = clothing_recommendation_elif(temperature)
    print("\n\n-------------- Using elif statements --------------")
    print(recommendation_if)

    # Using the second function with nested if statements
    recommendation_nested_if = clothing_recommendation_nested(temperature)
    print("\n\n============== Using nested if statements ==============")
    print(recommendation_nested_if)

main()
