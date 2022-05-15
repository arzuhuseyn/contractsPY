import pathlib
from setuptools import setup
  
  

HERE = pathlib.Path(__file__).parent


README = (HERE / "README.md").read_text()
  
  
# There is no any requirements.
REQUIREMENTS = []
  
# some more details
CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    ]
  

setup(
    name='contractsPY',
    version='1.0.5',
    description='Python Business Transactions Library',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/arzuhuseyn/contractsPY',
    author='Arzu Huseynov',
    author_email='hi@arzuh.me',
    license='MIT',
    packages=['contractsPY'],
    classifiers=CLASSIFIERS,
    install_requires=REQUIREMENTS,
    keywords='railway-oriented usecases transactions contracts',
)