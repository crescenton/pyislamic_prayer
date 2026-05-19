from setuptools import setup, find_packages

setup(
    name="pyislamic-prayer",
    version="1.0.1",
    author="Syed Sajid Ul Haq",
    author_email="crescentononline@gmail.com",
    description="Open-source Islamic prayer times engine with madhabs, calculation methods, high-latitude rules, and Qibla direction",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/CRESCENTON/pyislamic-prayer",
    packages=find_packages(),
    license="MIT",
    keywords=[
        "islam",
        "prayer-times",
        "salah",
        "qibla",
        "astronomy",
        "madhab"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Religion",
    ],
    python_requires=">=3.8",
)
