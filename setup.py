import re

import setuptools

with open("src/multithread_processing/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r"__version__ = \"(.*?)\"", f.read()).group(1)

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="multithread_parallel_processing",
    version=version,
    author="VegetaIV",
    author_email="hoangthanhlamm@gmail.com",
    description="Library support parallel processing with multi-thread",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hoangthanhlamm/multithread_parallel_processing",
    project_urls={"Bug Tracker": "https://github.com/hoangthanhlamm/multithread_parallel_processing", },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'requests',
    ],
)
