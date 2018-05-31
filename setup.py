import setuptools

with open('README.md', 'r',encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="ohHTML2Markdown",
    version="0.1.1",
    description="A Python Libary for converting HTML to md.",
    long_description=long_description,
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