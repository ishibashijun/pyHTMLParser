pyHTMLParser
=========

### HTML parser

## Usage
```python
from pyHTMLParser.Query import Q_open, Q_close, Q

Q_open('example.com')

second_target_link = Q('a[href$="-target.html"]:nth-child(2)')
print(second_target_link.attr('href'))

>>> some-target.html

Q_close()
```

## Documentation
[API Docs](http://ishibashijun.github.io/pyHTMLParser/)

## LICENSE

[MIT](http://www.opensource.org/licenses/mit-license.php)