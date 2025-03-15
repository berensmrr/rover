import rclpy
from rclpy.node import Node
from joint_state_publisher_gui import JointStatePublisherGui

class JointStatePublisherGUI(Node):
    def __init__(self):
        super().__init__('joint_state_publisher_gui')
        self.publisher = self.create_publisher(JointState, 'joint_states', 10)
        self.timer = self.create_timer(0.1, self.publish_joint_state)

    def publish_joint_state(self):
        msg = JointState()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.name = ['joint1', 'joint2']  # Burada uygun eklemen gerekebilir
        msg.position = [0.0, 0.0]  # Pozisyonları buraya eklemen gerekebilir
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = JointStatePublisherGUI()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

