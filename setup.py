from setuptools import setup

setup(
    name='customer',
    packages=['customer'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)