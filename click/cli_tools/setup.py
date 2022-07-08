from setuptools import setup


setup (
    name='cli_tools',
    version='1.0',
    py_modules=['greeter'],
    install_requires=[
        'Click'
    ],
    entry_points={
        'console_scripts': [ 'greetings=greeter:greet',
                            'add=calculator:add',
                            'substract=calculator:substract'
                            ]
    }

)
