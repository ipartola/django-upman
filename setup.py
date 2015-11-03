import codecs
from setuptools import setup


with codecs.open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

version = '0.1.0'

setup(
    name='django-upman',
    packages=['django_upman'],
    version=version,
    description='Django uploads manager',
    long_description=readme,
    author='Igor Partola',
    author_email='igor@igorpartola.com',
    license='MIT License',
    keywords='Django uploads manager',
    install_requires=['django', 'Pillow'],
    package_data={'django_upman': [
        '../README.md',
        '../LICENSE',
    ]},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
