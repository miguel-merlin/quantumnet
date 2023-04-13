from setuptools import find_packages, setup

setup(name='quantumnet',
    package_data=find_packages(include=['quantumnet']),
    version='0.1.0',
    description='Python library for quantum computing',
    author='Miguel Merlin',
    author_email='mmerlin@stevens.edu',
    license='MIT',
    install_requires = [],
    setup_requires = [],
    )