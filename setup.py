import setuptools


setuptools.setup(
    name='randomproto',
    version='0.0.1',
    py_modules=('randomproto',),
    install_requires=[
        'protobuf>=3.6.0',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-mock',
    ],
    author='Yu-Ping Wu',
    author_email='yupingso@gmail.com',
    description='Random protobuf object generator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='protobuf proto message random generate generator',
    url='https://github.com/yupingso/randomproto',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
