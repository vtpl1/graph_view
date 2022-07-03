import glob
import os

from setuptools import find_packages, setup

from Cython.Build import cythonize  # isort:skip


def get_python_files():
    l = []
    for z in [
            y + os.path.sep + "*.py" for y in [
                x.replace(".", os.path.sep)
                for x in find_packages(exclude=["*.tests", "test", "session"])
            ]
    ]:
        l.extend(glob.glob(z))
    return [a for a in l if not a.endswith("__init__.py")]


setup(
    name='graph_view',
    version='1.0.0',
    packages=find_packages(
        exclude=["*.tests", "test", "tests", "session", "videos"]),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "graph_view = graph_view.main:main",
        ],
    },
    install_requires=[
        'flask',
    ],
    # ext_modules=cythonize(get_python_files(), language_level="3"),
)