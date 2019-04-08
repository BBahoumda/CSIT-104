def convertToKg(pound):
    return 1/0.454 * pound

def run():
    pound = eval(input("Enter a value: "))
    kilogram = convertToKg(pound)
    print (str(pound) + " pound = " + str(kilogram) + " Kilograms.")
