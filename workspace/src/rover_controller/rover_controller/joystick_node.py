import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoystickNode(Node):
    def __init__(self):
        super().__init__('joystick_node')
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.subscription = self.create_subscription(Joy, '/joy', self.joy_callback, 10)
        self.max_speed = 1.0  # Maksimum ileri/geri hız
        self.max_turn_speed = 1.0  # Maksimum sağa/sola dönüş hızı

    def joy_callback(self, msg):
        """Joystick girişlerini hız verisine dönüştürerek yayımlar."""
        cmd = Twist()
        cmd.linear.x = msg.axes[1] * self.max_speed  # İleri/geri hız
        cmd.angular.z = msg.axes[0] * self.max_turn_speed  # Dönüş hızı
        self.publisher.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    joystick_node = JoystickNode()
    rclpy.spin(joystick_node)
    joystick_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
