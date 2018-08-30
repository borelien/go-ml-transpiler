from setuptools import setup
from setuptools import find_packages
import os


def get_version():
    src_dir = os.path.abspath(os.path.dirname(__file__))
    ver_file = os.path.join(src_dir, 'go_ml_transpiler', 'VERSION')
    version = open(ver_file, 'r').readlines().pop()
    if isinstance(version, bytes):
        version = version.decode('utf-8')
    version = str(version).strip()
    return version


def get_requirements():
    src_dir = os.path.abspath(os.path.dirname(__file__))
    req_file = os.path.join(src_dir, 'requirements.txt')
    reqs = open(req_file, 'r').read().strip().split('\n')
    reqs = [req.strip() for req in reqs if 'git+' not in req]
    return reqs


setup(name='go-ml-transpiler',
      version=get_version(),
      description='Transpile machine learning models from Python to Go.',
      url='http://github.com/znly/go-ml-transpiler',
      author='Zenly, Inc.',
      author_email='hello@zen.ly',
      keywords=['xgboost'],
      packages=find_packages(),
      classifiers=[
          'Intended Audience :: Developers',
          'Intended Audience :: Education',
          'Intended Audience :: Science/Research',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Topic :: Scientific/Engineering',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      license='Apache 2.0',
      install_requires=get_requirements(),
      zip_safe=False)
