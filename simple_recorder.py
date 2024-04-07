import picamera
import time

resolution = (1920, 1080)
framerate = 24

# Initialize the camera
camera = picamera.PiCamera(resolution=resolution, framerate=framerate)

try:
    while True:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"video_{timestamp}.mp4"

        camera.start_recording(filename)
        print("Begin recording " + filename + " ...")

        camera.wait_recording(60)

        camera.stop_recording()
        print("... End recording " + filename + "\n")

except KeyboardInterrupt:
    camera.stop_recording()

finally:
    camera.close()
