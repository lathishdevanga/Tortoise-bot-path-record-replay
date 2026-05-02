from setuptools import setup
import os
from glob import glob

package_name = 'tortoisebot_gazebo'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
    ('share/ament_index/resource_index/packages',
     ['resource/tortoisebot_gazebo']),
    ('share/tortoisebot_gazebo', ['package.xml']),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='laxmi',
    maintainer_email='you@example.com',
    description='Gazebo launch and world setup for TortoiseBot',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [],
    },
)

