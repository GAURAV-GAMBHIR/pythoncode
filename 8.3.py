class Temperature:
    def __init__(self,f,c):
        self.f = f
        self.c = c
    def convertFahrenheit(self):
        return self.c*9/5 + 32
    def convertCelcius(self):
        return (self.
                f-32)*5/9

ob5 = Temperature(120,42)
print(" \n120 in Celcius : ",ob5.convertCelcius(),"\n42 in Fahrenheit : ",ob5.convertFahrenheit())
