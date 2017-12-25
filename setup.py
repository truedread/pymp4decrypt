from os.path import abspath, dirname, join
from setuptools import setup, find_packages
from sys import path as sys_path

dependencies = [
    'pycryptodomex',
    'pymp4'
]

dependency_links = [
    'https://github.com/truedread/pymp4/tarball/master'
]

srcdir = join(dirname(abspath(__file__)), 'src/')
sys_path.insert(0, srcdir)

setup(
    name='pymp4decrypt',
    version='0.0.1',
    description='A Python MP4 decrypter for CENC encrypted MP4s',
    url='https://github.com/truedread/pymp4decrypt',
    author='truedread',
    author_email='truedread11@gmail.com',
    license='GNU GPLv3',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=dependencies,
    dependency_links=dependency_links,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Multimedia :: Sound/Audio',
        'Topic :: Multimedia :: Video',
        'Topic :: Utilities'
    ]
)