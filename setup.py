import setuptools

setuptools.setup(
    name="json_datatypes",
    version="0.1.0",
    url="https://github.com/kbaskett248/json-datatypes",

    author="Kenny Baskett",
    author_email="kbaskett248@gmail.com",

    description="A json parser, validator and serializer based on type annotations",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
