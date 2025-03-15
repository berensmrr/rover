from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Joystick Node
        Node(
            package='rover_controller',
            executable='joystick_node',
            name='joystick_node'
        ),
        # Camera Node
        Node(
            package='rover_controller',
            executable='camera_node',
            name='camera_node'
        ),
        # Rover Control Node
        Node(
            package='rover_controller',
            executable='rover_control_node',
            name='rover_control_node'
        ),
        # Robot State Publisher Node (URDF Dosyasını Yükle)
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': '$(find rover_controller)/urdf/rover.urdf'}]
        ),
        # Joint State Publisher Node (Eklemler için Yayıncı)
        Node(
            package='joint_state_publisher_gui',  # Eğer GUI kullanıyorsanız
            executable='joint_state_publisher_gui',
            name='joint_state_publisher'
        ),
    ])

