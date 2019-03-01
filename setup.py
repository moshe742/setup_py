from setuptools import setup, find_packages

setup(
    maintainer="maintainer name",
    maintainer_email="maintainer@example.com",
    name="HelloWorld"
    version="0.1",
    packages=find_packages(),
    description="this is a description",
    long_description="this is a very long description in markdown",
    url="URL",
    license="GPL",
    test_suite="tests",
    tests_require=["mock"],
    zip_safe=False,
    python_requires="2.7, 3.6",
    project_urls={
        "bug tracker": "URL",
        "documentation": "URL"
    }
    entry_points={
        'console_scripts': [
            'hello': 'hello_world:main'
        ]
    }
)
