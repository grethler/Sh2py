from setuptools import find_packages, setup

setup(
    name='shtwopy',
    packages=find_packages(include=['shtwopy']),
    version='0.1.0',
    description='Convert a python script into a decrypted shell script and vice versa.',
    author='Florian Grethler',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
