

# src/device_control/smartlight_deviceControl.py
import tkinter as tk

from src.device_control.device_control import DeviceControl
# ... (rest of your SmartLightDeviceControl implementation)

class SmartLightDeviceControl(DeviceControl):
    def create_controls(self):
        """ Creates controls for the Smart Light Device. """
        # Button to toggle on/off light
        self.toggle_button = tk.Button(self, text="Toggle Light", command=self.toggle_device)
        self.toggle_button.pack()

        # Scroll bar to set brightness
        self.brightness_scale = tk.Scale(self, from_=0, to=100, orient="horizontal", command=self.set_brightness)
        self.brightness_scale.set(self.device.brightness)  # Assuming 'brightness' attribute in SmartLight
        self.brightness_scale.pack()

    def set_brightness(self, level):
        """ Sets the brightness of the smart light. """
        self.device.set_brightness(int(level))  # Assuming 'set_brightness' method in SmartLight

    def update_controls(self):
        """ Updates the controls for the smart light. """
        # Update the brightness scale to reflect the current brightness
        self.brightness_scale.set(self.device.brightness)
