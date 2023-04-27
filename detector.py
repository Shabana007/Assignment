import threading
import time

class OfflineCameraDetector(threading.Thread):
    def __init__(self, camera_id):
        threading.Thread.__init__(self)
        self.camera_id = camera_id
        self.is_running = False
    
    def start_detection(self):
        self.is_running = True
        self.start()
    
    def stop_detection(self):
        self.is_running = False
    
    def run(self):
        while self.is_running:
            # Process the received camera data and perform offline camera detection
            # Implement your offline camera detection logic here
            print(f"Camera {self.camera_id}: Performing offline camera detection...")
            
            time.sleep(1)  # Simulate processing time

# Create camera detectors
detector1 = OfflineCameraDetector(1)
detector2 = OfflineCameraDetector(2)

# Start camera detection
detector1.start_detection()
detector2.start_detection()

# Wait for a specific duration (e.g., 10 seconds)
time.sleep(10)

# Stop camera detection
detector1.stop_detection()
detector2.stop_detection()

import pika
import cv2

# RabbitMQ configuration
RABBITMQ_HOST = 'localhost'
RABBITMQ_QUEUE = 'camera_tasks'

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue=RABBITMQ_QUEUE)


def process_camera_detection_task(message):
    # Perform camera detection task
    camera_input = cv2.VideoCapture(0) 

    while True:
        # Capture frame from the camera
        ret, frame = camera_input.read()

        # Process the frame and perform detection tasks
        # ...

        # Display the processed frame
        cv2.imshow("Camera Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera_input.release()
    cv2.destroyAllWindows()


     # Open the camera
    # Process the camera input and perform detection tasks
    # ...


# Define the callback function for consuming messages
def callback(ch, method, properties, body):
    # Process the received message
    process_camera_detection_task(body)
    print("Camera detection task processed:", body)


# Start consuming messages
channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback, auto_ack=True)

print("Waiting for camera detection tasks. To exit, press CTRL+C")
channel.start_consuming()
