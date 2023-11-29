import random

def random_motion_detection():
    """
    Simulates random motion detection.

    Returns:
    bool: True if motion is detected, False otherwise.
    """
    # Simulate motion detection (50% chance)
    return random.choice([True, False])

def random_temperature_change():
    """
    Simulates a random temperature change.

    Returns:
    float: A new temperature value.
    """
    # Generate a random temperature between, say, 15 and 30 degrees
    return random.uniform(1, 100)
