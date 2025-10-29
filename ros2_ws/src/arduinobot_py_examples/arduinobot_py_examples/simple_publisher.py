import rclpy # To import ros2 funtionalities within python script

from rclpy.node import Node # importing Node class

from std_msgs.msg import String

class SimplePublisher(Node):    # inheriting Node class, intialize components of base/node class
    def __init__(self):
        super().__init__("simple_publisher") # calling constructor of Node class & assigning name to node
        self.pub = self.create_publisher(String, "chatter", 10) # assigning type of msg, topic name and msg buffer(used in case of limit for subscribers if not processing msgs fast enough)

        self.counter = 0; # display no of msg published
        self.frequency = 1.0 # display no of msgs published in 1 sec in topic "chatter"
        self.get_logger().info("Publishing at %d Hz" % self.frequency) # displaying info in terminal
        self.timer = self.create_timer(self.frequency, self.timerCallBack) # to execute a certain function at a particular frequency

    def timerCallBack(self):
        msg = String() # type of msg
        msg.data = "Hello ROS 2 - counter: %d " % self.counter # msg value
        self.pub.publish(msg) # to publish the msg using object
        self.counter += 1 # increment counter value


def main():
    rclpy.init() # intializing rclpy library
    simple_publisher_obj = SimplePublisher() # object for class Simple Publisher
    rclpy.spin(simple_publisher_obj) # To execute continously
    simple_publisher_obj.destroy_node() # to stop/destroy node
    rclpy._shutdown()# to stop ROS


if __name__ == '__main__':
    main()





