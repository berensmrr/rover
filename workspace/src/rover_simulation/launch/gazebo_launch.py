from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

def generate_launch_description():
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join('/opt/ros/humble/share/gazebo_ros/launch', 'gazebo.launch.py')
        )
    )

    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'rover', '-file', os.path.join(os.getcwd(), 'urdf', 'rover.urdf')],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_entity
    ])
