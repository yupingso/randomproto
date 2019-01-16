import setuptools


setuptools.setup(
    name='randomproto',
    version='0.0.1rc2',
    py_modules=('randomproto',),
    install_requires=[
        'protobuf>=3.6.0',
    ],
    author='Yu-Ping Wu',
    author_email='yupingso@gmail.com',
    description='Random protobuf object generator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    keywords='protobuf proto message random generate generator',
    url='https://github.com/yupingso/randomproto',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
