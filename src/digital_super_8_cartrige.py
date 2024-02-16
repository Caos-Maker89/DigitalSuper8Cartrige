import time
import picamera
import RPi.GPIO as GPIO

# Set up GPIO
IR_SENSOR_PIN = 17  # Example GPIO pin for IR sensor
BUTTON_PIN = 18     # Example GPIO pin for button
RECORDING_PATH = "/path/to/recordings/"  # Change this to your desired path

GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize camera
camera = picamera.PiCamera()


def record_video():
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{RECORDING_PATH}video_{timestamp}.h264"
    camera.start_recording(filename)
    print(f"Recording video to {filename}")


def stop_recording():
    camera.stop_recording()
    print("Recording stopped")


def main():
    button_state = False
    motion_detected = False
    recording = False

    while True:
        # Check button state
        new_button_state = GPIO.input(BUTTON_PIN)
        if new_button_state != button_state:
            button_state = new_button_state
            if button_state:
                print("Button is ON")
            else:
                print("Button is OFF")
                if recording:
                    stop_recording()
                    recording = False

        # Check motion
        if GPIO.input(IR_SENSOR_PIN):
            print("Motion detected")
            motion_detected = True
        else:
            print("No motion detected")
            motion_detected = False

        # Start/stop recording based on conditions
        if button_state and motion_detected and not recording:
            record_video()
            recording = True
        elif (not button_state or not motion_detected) and recording:
            stop_recording()
            recording = False

        time.sleep(0.1)


if __name__ == "__main__":
    try:
        main()
    finally:
        GPIO.cleanup()
