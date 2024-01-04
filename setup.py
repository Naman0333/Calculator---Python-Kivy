from setuptools import setup

setup(
    name='CalculatorApp',
    version='1.0',
    packages=['calculator'],
    install_requires=[
        'kivy==2.1.0',
        'kivy.deps.glew==0.3.0',
        'kivy.deps.sdl2==0.3.1'
    ],
    entry_points={
        'console_scripts': [
            'calculatorapp = calculator.main:main'
        ],
    },
    options={
        'build_apps': {
            'kivy_icon': 'icon.png',
        }
    }
)
