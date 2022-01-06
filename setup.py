from setuptools import setup

with open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

setup(
    name="rapidfuzz_capi",
    version="0.0.1",
    url="https://github.com/maxbachmann/RapidFuzz",
    author="Max Bachmann",
    author_email="pypi@maxbachmann.de",
    description="capi to build extensions for rapidfuzz",
    long_description=readme,
    long_description_content_type="text/markdown",

    license="MIT",
    classifiers=[
        'Programming Language :: C',
        'Programming Language :: C++',
        'Programming Language :: Fortran',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools'
    ],
    packages=["rapidfuzz_capi"],
    zip_safe=True,
    include_package_data=True
)