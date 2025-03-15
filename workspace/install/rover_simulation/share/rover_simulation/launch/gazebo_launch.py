from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os

def generate_launch_description():
    # Gazebo'yu başlatan dosyayı ekle
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join('/home/vboxuser/rover_ws/install/rover_simulation/share/rover_simulation/launch', 'gazebo_launch.py')
        )
    )

    # URDF dosyasının yolunu belirt
    urdf_path = os.path.join('/home/vboxuser/rover_ws/src/rover_controller/urdf', 'rover.urdf')

    # Entity'yi sahnede başlat
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'rover', '-file', urdf_path],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_entity
    ])

