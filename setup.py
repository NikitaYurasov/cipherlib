from setuptools import setup, find_packages

setup(
    name='cipherlib',
    version="0.1",
    description='Block Ciphers',
    python_requires='>=3.6',
    author='MIEM',
    author_email='n.yurasov@yahoo.com',
    license='MIT',
    package_data={
        'ciphers': ['configs/logging_config.json'],
    },
    packages=find_packages(include=[
        'ciphers', 'ciphers.*'
    ]),
    include_package_data=True,
    zip_safe=False
)