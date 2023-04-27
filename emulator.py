import threading
import time

class CameraEmulator(threading.Thread):
    def __init__(self, camera_id):
        threading.Thread.__init__(self)
        self.camera_id = camera_id
        self.is_running = False
    
    def start_emulation(self):
        self.is_running = True
        self.start()
    
    def stop_emulation(self):
        self.is_running = False
    
    def run(self):
        while self.is_running:
            # Simulate camera behavior by capturing images or videos
            # Implement your camera emulation logic here
            print(f"Camera {self.camera_id}: Capturing image...")
            
            time.sleep(1)  # Simulate delay between image captures

# Create camera emulators
camera1 = CameraEmulator(1)
camera2 = CameraEmulator(2)

# Start camera emulation
camera1.start_emulation()
camera2.start_emulation()

# Wait for a specific duration (e.g., 10 seconds)
time.sleep(10)

# Stop camera emulation
camera1.stop_emulation()
camera2.stop_emulation()

