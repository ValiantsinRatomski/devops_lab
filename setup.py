from setuptools import setup, find_packages

setup(
    name="system_monitoring",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = system.system:main",
        ],
    },
    install_requires=[
        # put your requirements separated by comma here
    ],
    version="0.2",
    author="vratomski",
    author_email="vratomski@gmail.com",
    description="Example of the test application",
    license="MIT",
)
