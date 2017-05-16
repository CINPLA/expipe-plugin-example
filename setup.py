from setuptools import setup

from setuptools import setup, find_packages

setup(
    name="my-plugin",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'plugin-expipe-superduper = my_plugin.my_plugin_loader:reveal'
        ]
    }
)
