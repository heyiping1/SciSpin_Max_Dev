### Using continuous focus

from picamera2 import Picamera2
from libcamera import controls

# Create an object, picam2 which we will use as a link between the code and our camera.
picam2 = Picamera2()
# Start a preview window. The preview is where we see the output of the camera.
picam2.start(show_preview=True)
# Set the AfMode (Autofocus Mode) to be continuous.
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})