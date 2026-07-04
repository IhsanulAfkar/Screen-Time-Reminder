# Screen Time Reminder Application

This application tracks screen time usage and provides warnings when extended periods of screen time are detected.

Yes, this is 95% AI Slop.

## Features

- Real-time screen time tracking
- Visual warning display when screen time exceeds threshold (25 minutes)
- Console output for warnings
- Integration with webcam feed display

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- PySide6

## Installation

1. Install required packages:
   ```bash
   pip install opencv-python PySide6
   ```

2. Run the application:
   ```bash
   python app.py
   ```

## How It Works

1. The application starts tracking screen time when launched
2. A webcam feed is displayed in the window
3. Screen time is shown in real-time at the top of the window
4. When screen time exceeds 25 minutes, a warning appears:
   - On-screen warning message
   - Console output with "Screen time limit exceeded! Take a break."

## Files

- `app.py` - Main application with UI and screen time tracking
- `config.py` - Screen time management class
- `test_screen_time.py` - Test script for verifying functionality

## Customization

You can modify the warning threshold in `config.py` by changing the `warning_threshold` value.