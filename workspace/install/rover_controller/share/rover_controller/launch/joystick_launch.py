from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rover_controller',
            executable='joystick_node',
            name='joystick_node',
            output='screen'
        ),
    ])
