import rclpy
import RPi.GPIO as GPIO
from rclpy.node import Node
from std_msgs.msg import Int16

class ListenerNode(Node):

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(40, GPIO.OUT)

    def __init__(self):
        super().__init__("Listener")
        self.create_subscription(Int16, "countup", self.cb, 10)

    def cb(self, msg):
        self.get_logger().info("Listen: %d" % msg.data)
        if (msg.data % 3) == 0:
            GPIO.output(40, 1)
        else:
            GPIO.output(40, 0)
    


rclpy.init()
rclpy.spin( ListenerNode() )
