# src/device_control/smartlight_deviceControl.py
import tkinter as tk

from src.device_control.device_control import DeviceControl
# ... (rest of your SmartLightDeviceControl implementation)



class SecurityCameraDeviceControl(DeviceControl):
    def create_controls(self):
        """ Creates controls for the Security Camera. """
        # Button to toggle on/off recording
        self.toggle_button = tk.Button(self, text="Toggle Recording", command=self.toggle_device)
        self.toggle_button.pack()

        # Label to show motion status
        self.motion_label = tk.Label(self, text="Motion: Unknown")
        self.motion_label.pack()

    def update_controls(self):
        """ Updates the controls for the security camera. """
        # Update the motion detection label
        motion_status = "Detected" if self.device.is_motion_detected() else "No Motion"
        self.motion_label.config(text=f"Motion: {motion_status}")

    def update_motion_detection(self):
        """ Update the motion detection label to reflect the current status. """
        self.update_controls()

# Assuming SecurityCamera has a method is_motion_detected
