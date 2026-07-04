from config import ScreenTimeManager
import time

# Test the screen time manager
manager = ScreenTimeManager()
manager.start_session()

print("Screen time tracking started.")
print("Checking screen time...")

# Check initial state
print(f"Initial screen time: {manager.get_current_screen_time():.2f} minutes")

# Wait a few seconds to simulate usage
print("Simulating 3 seconds of usage...")
time.sleep(3)

# Check after some time
print(f"Screen time after 3 seconds: {manager.get_current_screen_time():.2f} minutes")

# Test warning system
if manager.check_warning():
    print("Warning triggered!")
else:
    print("No warning yet.")

print("Test completed.")