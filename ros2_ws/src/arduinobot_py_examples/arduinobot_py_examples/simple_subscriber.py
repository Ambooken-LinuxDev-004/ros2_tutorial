import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class SimpleSubscriber(Node):
    def __init__(self):
        super().__init__("simple_subscriber")
        self.sub = self.create_subscription(String, "chatter", self.msgCallBack, 10)

    def msgCallBack(self, msg):
        self.get_logger().info("I heard %s" % msg.data)




def main():
    rclpy.init()
    simple_subscriber_obj = SimpleSubscriber()
    rclpy.spin(simple_subscriber_obj)
    simple_subscriber_obj.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()



