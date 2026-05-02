from setuptools import setup
import os
from glob import glob

package_name = 'tortoisebot_description'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
    ('share/ament_index/resource_index/packages',
     ['resource/tortoisebot_description']),
    ('share/tortoisebot_description', ['package.xml']),
],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='laxmi',
    maintainer_email='you@example.com',
    description='URDF and RViz setup for TortoiseBot',
    license='MIT',
    tests_require=['pytest'],
        entry_points={
        'console_scripts': [
            # Optional if you have executables
            # 'my_node = my_package.my_node:main',
        ],
        'ament_index_python': [
            'tortoisebot_description = tortoisebot_description',
        ],
    },
)
