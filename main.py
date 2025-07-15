# main.py

from utils import calculate_sum, get_user_data, log_event

def run_application():
    result = calculate_sum(11, 0)
    print(f"Sum: {result}")

    user = get_user_data(123)
    print(f"User data: {user}")

    # application start
    log_event("Application Start", {"version":2.0})


if __name__ == "__main__":
    run_application()
