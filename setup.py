from setuptools import setup, find_packages

setup(
    name='FishTank',
    version='1.0.0',
    description='Fish Tank',
    url='https://github.com/bart-lute',
    author='Bart Lute',
    author_email='bart.lute@gmail.com',
    packages=find_packages(),
    install_requires=[
        'click',
        'pygame'
    ],
    entry_points={
        'console_scripts': [
            'fishtank=fishtank:fish_tank'
        ]
    }
)