from setuptools import setup, find_packages

setup(
    name="api-testing-project",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pytest>=7.4.0",
        "requests>=2.31.0",
        "jsonschema>=4.17.3",
        "pytest-html>=4.1.1",
        "pytest-cov>=4.1.0",
    ],
    python_requires=">=3.8",
) 