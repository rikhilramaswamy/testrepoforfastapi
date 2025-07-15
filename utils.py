# utils.py

def calculate_sum(a, b):
    # helper to do basic addition 
    return a + b


def log_event(event_name: str, details: dict = {}):
    """Logs a new event."""
    log_entry = {"event": event_name, "details": details}
    print(f"Logging event: {log_entry}")
    return log_entry

class Helper:
    def __init__(self, value):
        self.value = value

    def process(self):
        """Processes the helper's value."""
        return self.value * 2
