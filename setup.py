from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="pybasic",
    author="Lorenz Lamm, Tingying Peng, Mohammad Mirkazemi",
    author_email="tingying.peng@helmholtz-muenchen.de, Lorenz.lamm@helmholtz-muenchen.de",
    keywords="Background Shading Flatfield Darkfield Biology Optical Microscopy Image",
    install_requires=[
        l.strip() for l in Path("requirements.txt").read_text("utf-8").splitlines()
    ],
    package_dir={"pybasic": "pybasic", "pybasic.tools": "pybasic/tools"},
    packages=["pybasic", "pybasic.tools"],
    include_package_data=True,
)
