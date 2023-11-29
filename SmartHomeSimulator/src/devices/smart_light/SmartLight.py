#from src.devices.smart_device import SmartDevice
import random

class SmartLight:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = "off"
        self.brightness = 0

    def setBrightness(self, brightness):
        self.brightness = brightness

    def turn_on(self):
        self.status = "on"
        self.brightness = random.randint(1, 100)

    def turn_off(self):
        self.status = "off"
        self.brightness = 0

    def dim(self):
        if self.status == "on":
            self.brightness = max(0, self.brightness - random.randint(1, 3))