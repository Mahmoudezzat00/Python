class AutomationRule:
    def __init__(self, name):
        self.name = name

    def evaluate(self, automationSystem):
        """
        Evaluate and apply the rule.

        Parameters:
        automationSystem: Instance of AutomationSystem where the rule will be applied.
        """
        raise NotImplementedError("This method should be implemented by subclasses.")
