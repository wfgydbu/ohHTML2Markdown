from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

setup(
    name="ohHTML2Markdown",
    version="0.1",
    description="A Python Libary for converting HTML to md.",
    long_description=readme,
    author="Ethan Huang",
    author_email="wfgydbu@163.com",
    url='https://github.com/wfgydbu/ohHTML2Markdown',
    license='GNU GPL 3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=['beautifulsoup4==4.6.0'],
)