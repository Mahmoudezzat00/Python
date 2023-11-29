
from src.devices.smart_light import SmartLight
from src.devices.thermostat import Thermostat
from src.devices.security_camera import SecurityCamera

import tkinter as tk
from tkinter import ttk

class DeviceGUI(tk.Frame):
    def __init__(self, master, device, system, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.device = device
        self.system = system
        self.init_ui()

    def init_ui(self):
        self.label = tk.Label(self, text=f"{self.device.device_id}: status={self.device.status}")
        self.label.grid(row=0, column=0, sticky='ew')

        if isinstance(self.device, SmartLight) or isinstance(self.device, Thermostat):
            self.scale = tk.Scale(self, from_=0, to=100, orient='horizontal', command=self.change_level)
            self.scale.grid(row=1, column=0, sticky='ew')
            self.scale.set(0)  # Default to 0 for both brightness and temperature

        self.on_button = tk.Button(self, text="Turn On", command=self.turn_on)
        self.on_button.grid(row=2, column=0)

        self.off_button = tk.Button(self, text="Turn Off", command=self.turn_off)
        self.off_button.grid(row=3, column=0)

        if isinstance(self.device, SecurityCamera):
            self.detect_button = tk.Button(self, text="Detect", command=self.detect)
            self.detect_button.grid(row=4, column=0)

        # Styling
        self.columnconfigure(0, weight=1)  # Make the scale fill the frame

    def change_level(self, value):
        value = int(value)
        if isinstance(self.device, SmartLight):
            self.device.setBrightness(value)
        elif isinstance(self.device, Thermostat):
            self.device.setTemperature(value)
        self.update_label()

    def turn_on(self):
        self.device.turn_on()
        self.update_label()

    def turn_off(self):
        self.device.turn_off()
        self.update_label()

    def detect(self):
        if isinstance(self.device, SecurityCamera):
            self.device.detect()
        self.update_label()

    def update_label(self):
        status = f"{self.device.device_id}: status={self.device.status}"
        if isinstance(self.device, SmartLight):
            status += f", brightness={self.device.brightness}"
        elif isinstance(self.device, Thermostat):
            status += f", temperature={self.device.temperature}"
        elif isinstance(self.device, SmartLight):
            status += f", brightness={self.device.brightness}"
        self.label.config(text=status)