#from src.devices.smart_device import SmartDevice
import random

class Thermostat:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = "off"
        self.temperature = 0

    def setTemperature(self, temperature):
        self.temperature = temperature

    def turn_on(self):
        self.status = "on"
        self.temperature = random.randint(0, 5)

    def turn_off(self):
        self.status = "off"
        self.temperature = 0

    def heat_up(self):
        if self.status == "on":
            self.temperature = min(30, self.temperature + random.randint(1, 3))