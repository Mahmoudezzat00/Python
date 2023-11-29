# Assuming SmartDevice is defined in the devices package
#from src.devices.smart_device import SmartDevice
# Assuming random_motion_detection is defined in the utils module
#from src.utils import random_motion_detection
import random

class SecurityCamera:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = "off"
        self.security_status = "idle"

    def turn_on(self):
        self.status = "on"
        self.security_status = random.choice(["idle", "alert"]) # random security status

    def turn_off(self):
        self.status = "off"

    def detect(self, system):
        if self.status == "on":
            system.turn_on_lights()
