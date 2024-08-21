from setuptools import find_packages, setup
setup(
    name="bash_virtual_env_dagster",
    packages=find_packages(exclude=["bash_virtual_env_dagster_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-pipes",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
