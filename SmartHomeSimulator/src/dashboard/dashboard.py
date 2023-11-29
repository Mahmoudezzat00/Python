import tkinter as tk

class Dashboard(tk.Frame):
    def __init__(self, master, system):
        super().__init__(master)
        self.system = system
        self.master = master

        # Attributes
        self.currentDeviceControl = None
        self.device_listbox = None
        self.controls_frame = None
        self.control_factory = None  # Assuming you have a ControlFactory class

        self.create_widgets()

    def create_widgets(self):
        """ Initializes and places the base widgets on the dashboard frame. """

        # Listbox for devices
        self.device_listbox = tk.Listbox(self)
        self.device_listbox.bind('<<ListboxSelect>>', self.on_device_select)
        self.device_listbox.pack(side="left", fill="y")

        # Frame for device controls
        self.controls_frame = tk.Frame(self)
        self.controls_frame.pack(side="right", fill="both", expand=True)

        self.update_device_listbox()

    def on_device_select(self, event):
        """ Handles device selection from the listbox. """
        widget = event.widget
        index = int(widget.curselection()[0])
        device = self.system.devices[index]

        self.update_controls_frame(device)

    def update_controls_frame(self, device):
        """ Updates the controls frame with controls for the given device. """
        # Clear current controls
        for widget in self.controls_frame.winfo_children():
            widget.destroy()

        # Get new controls for the selected device
        self.currentDeviceControl = self.control_factory.create_control(self.controls_frame, device)
        self.currentDeviceControl.pack(fill="both", expand=True)

    def update_device_listbox(self):
        """ Refreshes the listbox items to reflect the current list of devices. """
        self.device_listbox.delete(0, tk.END)
        for device in self.system.devices:
            self.device_listbox.insert(tk.END, device.device_id)  # or some string representation of the device

    def update_dashboard(self):
        """ Refreshes the entire dashboard. """
        self.update_device_listbox()
        # Update other dashboard elements as necessary
