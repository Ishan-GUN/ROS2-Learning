#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
class TurtleController(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("turtle_controller") # MODIFY NAME
        self.vel_publisher_ = self.create_publisher(Twist,"turtle1/cmd_vel",10)
        self.pose_subscriber_ = self.create_subscription(Pose,"turtle1/pose",self.pose_callback,10)
    def pose_callback(self,msg):
        self.get_logger().info("Pose: x="+str(msg.x)+" y="+str(msg.y)+" theta="+str(msg.theta)) 
        a = Twist()
        if msg.x>5.5:
            a.linear.x=2.0
            a.angular.z=2.0
        else:
            a.linear.x=1.0
            a.angular.z=1.0
        self.vel_publisher_.publish(a)
        
    
    
def main(args=None):
    rclpy.init(args=args)
    node = TurtleController() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()
if __name__ == "__main__":
    main()