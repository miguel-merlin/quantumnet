from setuptools import find_packages, setup

setup(name='quantumnet',
    version='0.1.0',
    description='Python library for quantum computing',
    author='Miguel Merlin',
    author_email='mmerlin@stevens.edu',
    license='MIT',
    package_dir={'':'src'},
    packages= find_packages(where='src'),
    )