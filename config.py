import time
from datetime import datetime, timedelta

class ScreenTimeManager:
    def __init__(self):
        self.start_time = None
        self.total_screen_time = 0
        self.warning_shown = False
        self.warning_threshold = 25  # Warning at 25 minutes
        
    def start_session(self):
        """Start tracking screen time"""
        self.start_time = datetime.now()
        self.warning_shown = False
        
    def get_current_screen_time(self):
        if self.start_time:
            elapsed = datetime.now() - self.start_time
            return elapsed.total_seconds() + self.total_screen_time

        return self.total_screen_time
    
    def add_session_time(self, minutes):
        """Add time to total screen time (for when app is closed and reopened)"""
        self.total_screen_time += minutes
        
    def check_warning(self):
        """Check if warning should be shown"""
        current_time = self.get_current_screen_time()
        return current_time >= self.warning_threshold
    
    def reset_session(self):
        """Reset the session and start fresh - this resets only the current timer"""
        # Reset just the current session time, not the total
        self.start_time = datetime.now()
        self.warning_shown = False
        print("Screen time timer reset due to face detection.")
        
    def end_session(self):
        """End current session and update total time"""
        if self.start_time:
            elapsed = datetime.now() - self.start_time
            self.total_screen_time += elapsed.total_seconds() / 60
            self.start_time = None
            
    def set_warning_threshold(self, minutes):
        """Set custom warning threshold in minutes"""
        self.warning_threshold = minutes
        
    def get_current_time(self):
        """Get current time for display purposes"""
        return self.get_current_screen_time()
    
    def get_treshold_timer(self):
        # 20 minutes
        return 20*60

