from setuptools import setup, Command
import pybloomd

# Get the long description by reading the README
try:
    readme_content = open("README.rst").read()
except:
    readme_content = ""

# Create the actual setup method
setup(name='pybloomd',
      version=pybloomd.__version__,
      description='A fork from https://github.com/kiip/bloom-python-driver/, which is compatiable with Python 3',
      long_description=readme_content,
      author='Armon Dadgar',
      author_email='biz@kiip.me',
      maintainer='Xrazor',
      maintainer_email='xrazor1031@gmail.com',
      url="https://github.com/xrazor1031/bloom-python-driver",
      license="MIT License",
      keywords=["bloom", "filter", "client", "bloomd"],
      py_modules=['pybloomd'],
      classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Database",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
    ]
      )
