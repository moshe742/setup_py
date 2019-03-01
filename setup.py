from setuptools import setup, find_packages

setup(
    maintainer="maintainer name",
    maintainer_email="maintainer@example.com",
    name="HelloWorld"
    version="0.1",
    packages=find_packages(),
    description="this is a description",
    long_description="this is a very long description in markdown",
    download_url="URL",
    license="GPL",
    test_suite="tests",
    tests_require=["mock"],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'hello': 'hello_world:main'
        ]
    }
)
