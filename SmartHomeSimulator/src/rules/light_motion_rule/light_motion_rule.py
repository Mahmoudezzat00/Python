from src.rules.automation_rule import AutomationRule

class LightMotionRule(AutomationRule):
    def __init__(self, name, camera_device_id, light_device_id):
        super().__init__(name)
        self.camera_device_id = camera_device_id
        self.light_device_id = light_device_id

    def evaluate(self, system):
        """
        Evaluates the rule and turns on the light if motion is detected by the camera.

        Parameters:
        system: An instance of the automation system where this rule is applied.
        """
        camera = system.get_device_by_id(self.camera_device_id)
        light = system.get_device_by_id(self.light_device_id)

        if camera and light and camera.is_motion_detected():
            light.turn_on()
