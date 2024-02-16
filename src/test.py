import unittest
from unittest.mock import patch, MagicMock
import time

from digital_super_8_cartrige import *


class TestRecordVideo(unittest.TestCase):
    @patch('time.strftime', return_value='20240216-143000')
    @patch('builtins.print')
    @patch('picamera.PiCamera')
    def test_record_video(self, mock_camera, mock_print, mock_strftime):
        RECORDING_PATH = "/path/to/recordings/"
        mock_camera_instance = MagicMock()
        mock_camera.return_value = mock_camera_instance

        record_video()

        mock_camera_instance.start_recording.assert_called_once_with(
            '/path/to/recordings/video_20240216-143000.h264')
        mock_print.assert_called_once_with(
            'Recording video to /path/to/recordings/video_20240216-143000.h264')


class TestStopRecording(unittest.TestCase):
    @patch('picamera.PiCamera')
    def test_stop_recording(self, mock_camera):
        mock_camera_instance = MagicMock()
        mock_camera.return_value = mock_camera_instance

        stop_recording()

        mock_camera_instance.stop_recording.assert_called_once()


class TestMainMethod(unittest.TestCase):
    @patch('your_script_name.GPIO')
    @patch('your_script_name.picamera.PiCamera')
    def test_main(self, mock_camera, mock_gpio):
        # Mock the input states and function calls
        # Simulate button state changes
        mock_gpio.input.side_effect = [True, False, True, False]
        mock_gpio.IN = GPIO.IN
        mock_camera_instance = MagicMock()
        mock_camera.return_value = mock_camera_instance

        # Call the main function
        main()

        # Ensure camera methods are called correctly
        mock_camera_instance.start_recording.assert_called_once()
        mock_camera_instance.stop_recording.assert_called_once()


if __name__ == '__main__':
    unittest.main()
