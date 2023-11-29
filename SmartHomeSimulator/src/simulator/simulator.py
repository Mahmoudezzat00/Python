import tkinter as tk
import threading
import time

class Simulator(threading.Thread):
    def __init__(self, root, system, dashboard, update_callback):
        super().__init__()
        self.root = root
        self.system = system
        self.dashboard = dashboard
        self.update_callback = update_callback
        self.is_running = False

    def setup(self):
        """ Prepares the simulation environment. """
        self.dashboard.pack()  # Assuming the dashboard is a tk.Frame or similar widget

    def run(self):
        """ The main loop of the thread for the simulation. """
        self.is_running = True
        while self.is_running:
            # Execute automation rules
            self.system.execute_automation_rules()

            # Update the GUI
            if self.update_callback:
                self.update_callback()

            # Sleep for a short time to avoid overloading the CPU
            time.sleep(3)

    def stop(self):
        """ Stops the simulation loop. """
        self.is_running = False
