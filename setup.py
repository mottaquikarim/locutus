from setuptools import find_packages, setup

setup(
    name='locutus',
    version='0.0.1',
    description='Home Automation scripts running on Lambda',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    zip_safe=True,
    setup_requires=['wheel'],
)
