import random
import tkinter as tk
from tkinter import ttk

# ... (Other device classes and AutomationSystem class)
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

class AutomationSystem:
    def __init__(self):
        self.devices = {}
    def add_device(self, device):
        self.devices[device.device_id] = device
    def remove_device(self, device_id):
        if device_id in self.devices:
            del self.devices[device_id]
    def discover_devices(self):
        return list(self.devices.keys())
    def turn_on_lights(self):
        for device in self.devices.values():
            if isinstance(device, SmartLight):
                device.turn_on()

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
            self.device.detect(system)
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

# ... (AutomationSystemGUI and System Initialization)
class AutomationSystemGUI:
    def __init__(self, system):
        self.system = system
        self.window = tk.Tk()
        self.devices_frame = tk.Frame(self.window)
        self.devices_frame.grid()
        self.device_guis = {}
        for i, device in enumerate(self.system.devices.values()):
            device_gui = DeviceGUI(device, self.devices_frame)
            device_gui.label.grid(row=i*5, column=0)
            device_gui.on_button.grid(row=i*5+1, column=0)
            device_gui.off_button.grid(row=i*5+2, column=0)
            if isinstance(device, SecurityCamera):
                device_gui.detect_button.grid(row=i*5+3, column=0)
            if isinstance(device, Thermostat) or isinstance(device, SmartLight):
                device_gui.range_bar.grid(row=i*5+4, column=0)
            self.device_guis[device.device_id] = device_gui
        self.window.after(3000, self.execute_loop)

    
        

    def run(self):
        self.window.mainloop()


# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Smart Home IoT Simulator")
    root.geometry("400x300")  # Set initial size of the window

    system = AutomationSystem()
    light = SmartLight("Living Room Light")
    thermostat = Thermostat("Living Room Thermostat")
    camera = SecurityCamera("Front Door Camera")

    system.add_device(light)
    system.add_device(thermostat)
    system.add_device(camera)

    main_frame = ttk.Notebook(root)  # Using Notebook for tabbed view
    main_frame.pack(expand=True, fill="both")

    # Create a tab for each type of device
    light_frame = ttk.Frame(main_frame)
    thermostat_frame = ttk.Frame(main_frame)
    camera_frame = ttk.Frame(main_frame)

    main_frame.add(light_frame, text="Lights")
    main_frame.add(thermostat_frame, text="Thermostats")
    main_frame.add(camera_frame, text="Cameras")

    # Add devices to their respective tabs
    DeviceGUI(light_frame, light, system).pack(fill="x", expand=True)
    DeviceGUI(thermostat_frame, thermostat, system).pack(fill="x", expand=True)
    DeviceGUI(camera_frame, camera, system).pack(fill="x", expand=True)

    root.mainloop()