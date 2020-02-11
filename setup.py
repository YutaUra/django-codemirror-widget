from setuptools import setup, find_packages

NAME = 'django-codemirror-widget'
VERSION = '0.4.1'


def read(filename):
    import os
    BASE_DIR = os.path.dirname(__file__)
    filename = os.path.join(BASE_DIR, filename)
    with open(filename, 'r') as fi:
        return fi.read()

 
def readlist(filename):
    rows = read(filename).split("\n")
    rows = [x.strip() for x in rows if x.strip()]
    return list(rows)

 
setup(
    name=NAME,
    version=VERSION,
    description="Django form widget library for using CodeMirror on textarea",
    long_description=read('README.rst'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords="django widget textarea codemirror",
    author="Yuta Ura",
    author_email="yuuta3594@outlook.jp",
    url="https://github.com/YutaUra/django-codemirror-widget-2",
    # download_url="https://github.com/YutaUra/%s/tarball/master" % NAME,
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
)
