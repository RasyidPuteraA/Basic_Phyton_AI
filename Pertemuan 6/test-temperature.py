class data_attributes:
    def __init__(self, celcius):
        self.celcius = celcius

    def temperature_monitor(self):
        print("Temperatur celcius: ", int(self.celcius))
    def fahrenheit(self):
        f = 9/5 * self.celcius +32
        print(f)
    def reamur(self):
        r = 4/5 * self.celcius
        print(r)
    def kelvin(self):
        k = self.celcius + 273
        print(k)


suhu = data_attributes(int(input("Masukkan nilai suhu: ")))
suhu.temperature_monitor()
suhu.fahrenheit()
suhu.reamur()
suhu.kelvin()