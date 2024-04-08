import picamera
import time

resolution = (1920, 1080)
framerate = 24

camera = picamera.PiCamera(resolution=resolution, framerate=framerate)

# https://picamera.readthedocs.io/en/release-1.13/recipes1.html

# Set ISO to the desired value
camera.iso = 400
# Wait for the automatic gain control to settle
sleep(2)
# Now fix the values
camera.shutter_speed = camera.exposure_speed
camera.exposure_mode = 'off'
g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g

try:
    while True:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"video_{timestamp}.h264"

        camera.start_recording(filename)
        print("Begin recording " + filename + " ...")

        camera.wait_recording(60)

        camera.stop_recording()
        print("... End recording " + filename + "\n")

except KeyboardInterrupt:
    camera.stop_recording()

finally:
    camera.close()
