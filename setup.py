from setuptools import setup

version = '1.1.2'
name = 'pyHTMLParser'
short_description = 'A simple html parser/scraper/reader that constructs DOM tree.'
long_description = """\
A pyHTMLParser has chaining API and tested in Python 3.4.

Example
-------

.. code-block:: python

    from pyHTMLParser import *
    
    parser = pyHTMLParser()
    parser.open('http://www.example.com')
    links = parser.tag('a')
    for link in links:
        print(link.attr('href'))
    parser.close()

Some API
--------

pyHTMLParser

    tag - returns a pyNodeList matching a tag name

    id - returns a pyNode matching the provided ID

    cls - returns a pyNodeList containing a class name

pyNodeList

    eq - returns a single element at the specified index

    first - returns a first element of the html

    last - returns a last element of the html

pyNode

    name - returns a tab name

    cls - returns a class name(s)

    text - returns a text
"""

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Text Processing :: Markup :: HTML'
]

setup(
    name = name,
    version = version,
    description = short_description,
    long_description = long_description,
    classifiers = classifiers,
    license = 'MIT',
    keywords = ['parse', 'scrape', 'html',
                'parser', 'tree', 'DOM',
                'jquery'],
    author = 'Jun Ishibashi',
    author_email = 'ishibashijun@gmail.com',
    url = 'http://ishibashijun.github.io/'
)
