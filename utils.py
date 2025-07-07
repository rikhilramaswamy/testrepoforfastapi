# utils.py - Original Version

def calculate_sum(a, b):
    return a + b

def get_user_data(user_id):
    # TODO: Implement user data retrieval from DB
    data = {"id": user_id, "name": "John Doe"}
    return data

class Helper:
    def __init__(self, value):
        self.value = value

    def process(self):
        return self.value * 2
