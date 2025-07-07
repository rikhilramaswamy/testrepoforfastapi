# main.py - Original Version

from utils import calculate_sum, get_user_data

def run_application():
    result = calculate_sum(10, 5)
    print(f"Sum: {result}")

    user = get_user_data(123)
    print(f"User data: {user}")

if __name__ == "__main__":
    run_application()
