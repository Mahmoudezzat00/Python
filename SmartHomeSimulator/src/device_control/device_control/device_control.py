import tkinter as tk
from abc import ABC, abstractmethod

class DeviceControl(ABC, tk.Frame):
    def __init__(self, master, device, update_callback):
        super().__init__(master)
        self.device = device
        self.update_callback = update_callback

        self.create_controls()  # Call the abstract method to initialize controls

    @abstractmethod
    def create_controls(self):
        """
        Abstract method to create and layout GUI components.
        This method should be implemented by subclasses.
        """
        pass

    @abstractmethod
    def update_controls(self):
        """
        Abstract method to update the GUI components.
        This method should be implemented by subclasses to reflect the current state of the device.
        """
        pass

    def toggle_device(self):
        """
        Toggles the state of the associated device and invokes the update callback to refresh the GUI.
        """
        self.device.toggle_device()  # Assuming the device has a method named 'toggle_device'
        self.update_callback()       # Invoke the callback to update the GUI
