from setuptools import setup, find_packages

setup(
    name="RedPanda-transpiler",
    version="0.1.0",
    description="A Python to Mandarin Chinese transpiler.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="fmasterpro27",
    license="Apache-2.0",
    python_requires=">=3.11",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "redpanda": ["data/**/*.json"],
    },
    install_requires=[],
    entry_points={
        "console_scripts": [
            "redpanda=redpanda.cli:main",
        ],
    },
    keywords=[
        "python",
        "transpiler",
        "compiler",
        "parser",
        "mandarin",
        "chinese",
        "language",
        "codegen",
        "redpanda",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Interpreters",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    project_urls={
        "Homepage": "https://github.com/Fmasterpro27/RedPanda-transpiler",
        "Repository": "https://github.com/Fmasterpro27/RedPanda-transpiler",
        "Issues": "https://github.com/Fmasterpro27/RedPanda-transpiler/issues",
    },
)