class SmartDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False  # False: Off, True: On

    def turn_on(self):
        """ Sets the device's status to True (on). """
        self.status = True

    def turn_off(self):
        """ Sets the device's status to False (off). """
        self.status = False

    def toggle_device(self):
        """ Toggles the device's status between True and False. """
        self.status = not self.status

    def get_status(self):
        """
        Gets the current status of the smart device.
        
        Returns:
            bool: The current status of the device, where True represents on and False represents off.
        """
        return self.status
