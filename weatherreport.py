

def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }

def sensorStubHighPrecep():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 30,
        'windSpeedKMPH': 30
    }

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather


def testRainy():
    weather = report(sensorStub)
    print("testRainy result:", weather)
    assert("rain" in weather)


def testHighPrecipitation():
    weather = report(sensorStubHighPrecep)
    print("testHighPrecipitation result:", weather)
    assert("rain" in weather or "Partly" in weather or "Cloudy" in weather)

if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)");
