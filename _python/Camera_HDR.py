### Capture an HDR image with Picamera2

from picamera2 import Picamera2
from libcamera import controls
import os

# Create an object, picam2 which we will use as a link between the code and our camera.
picam2 = Picamera2()
os.system("v4l2-ctl --set-ctrl wide_dynamic_range=1 -d /dev/v4l-subdev0")
print("Setting HDR to ON")
# Start a preview window. The preview is where we see the output of the camera.
picam2.start(show_preview=True)
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous, "AfSpeed": controls.AfSpeedEnum.Fast})
picam2.start_and_capture_files("HDRfastfocus{:d}.jpg", num_files=3, delay=1)
picam2.stop_preview()
picam2.stop()
print("Setting HDR to OFF")
os.system("v4l2-ctl --set-ctrl wide_dynamic_range=0 -d /dev/v4l-subdev0")
