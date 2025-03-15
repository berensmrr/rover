from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='gzserver',
            name='gazebo_server',
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='gzclient',
            name='gazebo_client',
            output='screen'
        ),
        Node(
            package='rover_controller',
            executable='joystick_node',
            name='joystick_node'
        ),
        Node(
            package='rover_controller',
            executable='camera_node',
            name='camera_node'
        ),
        Node(
            package='rover_controller',
            executable='rover_control_node',
            name='rover_control_node'
        ),
    ])

