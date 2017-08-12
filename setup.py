from setuptools import setup

setup(
    name='Incubate',
    packages=['Incubate'],
    include_package_data=True,
    install_requires=[
        'flask', 'flask-session', 'flask-mail', 'flask-mysqldb', 'flask-cli'
    ],
)