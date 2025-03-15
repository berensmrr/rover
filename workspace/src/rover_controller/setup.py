import os
from glob import glob
from setuptools import setup

package_name = 'rover_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # launch dosyalarını ekleyin
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        # URDF dosyalarını da ekle
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Rover controller with ROS2 nodes',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joystick_node = rover_controller.joystick_node:main',
            'camera_node = rover_controller.camera_node:main',
            'rover_control_node = rover_controller.rover_control_node:main',
            # Yeni node'lar
            'joint_state_publisher_gui = rover_controller.joint_state_publisher_gui:main',  # joint_state_publisher_gui node'u
            'robot_state_publisher = rover_controller.robot_state_publisher:main',  # robot_state_publisher node'u
        ],
    },
)

