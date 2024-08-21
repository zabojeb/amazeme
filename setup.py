from setuptools import setup, find_packages

setup(
    name='amazeme',
    version='1.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'amazeme = amazeme.amazeme:main',
        ],
    },
    install_requires=[
        'click',
    ],
    python_requires='>=3.6',
    include_package_data=True,
    license='MIT',
    description='CLI utilite for generating and displaying mazes in the terminal',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/zabojeb/amazeme',
    author='zabojeb',
    author_email='zabojeb@bk.ru',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Games/Entertainment :: Puzzle Games',
    ],
)
