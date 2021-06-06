from setuptools import setup, find_packages

setup(name='image_tools',
    version='0.0.3',
    description='CLI tool for various image manipulation tasks.',
    url='https://github.com/dan-velez/image_tools',
    author='Daniel Velez',
    author_email='daniel.enr.velez@gmail.com',
    license='MIT,
    python_requires=">=3.6",
    packages=['image_tools'],
    entry_points={
        'console_scripts': ['image-tools=image_tools.__main__:main']
    },
    install_requires=['opencv-python==4.4.0.46'])