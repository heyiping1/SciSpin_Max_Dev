### Fast focus for multiple images

from picamera2 import Picamera2
from libcamera import controls

# Create an object, picam2 which we will use as a link between the code and our camera.
picam2 = Picamera2()
# Start a preview window. The preview is where we see the output of the camera.
picam2.start(show_preview=True)
# Set the autofocus mode to Continuous and set the AfSpeed to Fast.
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous, "AfSpeed": controls.AfSpeedEnum.Fast})
# Set the camera to capture three files, with a delay of half a second between each shot.
picam2.start_and_capture_files("fastfocus-test{:d}.jpg", num_files=3, delay=0.5)
# Close the preview window.
picam2.stop_preview()
# Close the camera connection.
picam2.stop()


