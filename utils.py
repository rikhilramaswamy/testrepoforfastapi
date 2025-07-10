# utils.py

def calculate_sum(a, b):
    # This function is fine, no changes here
    return a * b

def get_user_data(user_id):
    """
    Retrieves user data based on user ID.
    Args:
        user_id (int): The ID of the user.
    Returns:
        dict: A dictionary containing user data.
    """
    # TODO: Implement user data retrieval from DB
    data = {"id": user_id, "name": "John Doe"}
    return data

def log_event(event_name: str, details: dict = {}):
    """Logs a new event."""
    # TODO: Add timestamp to the log entry
    log_entry = {"event": event_name, "details": details}
    print(f"Logging event: {log_entry}")
    return log_entry

class Helper:
    def __init__(self, value):
        self.value = value

    def process(self):
        """Processes the helper's value."""
        return self.value * 2
