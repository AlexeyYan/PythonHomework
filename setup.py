from setuptools import setup

setup(
    name='rss_reader',
    version='2.0',
    description='Simple CLI RSS feed reader.',
    long_description='Simple CLI reeder for RSS feeds with basic fuctions.',
    url='https://github.com/AlexeyYan/PythonHomework',
    author='Aleksey Yanovich',
    author_email='yanovichaleksey@gmail.com',
    packages=["rss_reader"],
    python_requires='>=3.8',
    install_requires=['beautifulsoup4'],
    entry_points={
        'console_scripts': [
            'rss_reader=rss_reader:start_app'
        ]
    }
)
