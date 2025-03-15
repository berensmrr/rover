import rclpy
from rclpy.node import Node
from robot_state_publisher import RobotStatePublisher
from ament_index_python.packages import get_package_share_directory
from urdf_parser_py.urdf import URDF

class RobotStatePublisherNode(Node):
    def __init__(self):
        super().__init__('robot_state_publisher_node')

        # Robot URDF dosyasının yolunu al
        urdf_path = get_package_share_directory('rover_simulation') + '/urdf/robot.urdf'

        # URDF dosyasını yükle
        robot = URDF.from_xml_file(urdf_path)

        # Robot state publisher'ı başlat
        self.robot_state_publisher = RobotStatePublisher(self, robot)
        
        # Robot state publisher'ı başlat
        self.robot_state_publisher.publish()

def main(args=None):
    rclpy.init(args=args)

    node = RobotStatePublisherNode()

    # Node'u çalıştır
    rclpy.spin(node)

    # Node'u kapat
    rclpy.shutdown()

if __name__ == '__main__':
    main()

