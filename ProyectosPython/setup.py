from setuptools import setup, find_packages
setup(
    name= 'domain',
    extras_require=dict(test=['pytest']),
    packages=find_packages(where='src'),
    package_dir={"": "src"},
)