pyHTMLParser
=========

### HTML parser/scraper/reader

## Usage
```python
from pyHTMLParser.Parser import Parser

parser = Parser()
parser.open('http://www.example.com')
links = parser.tag('a')
for link in links:
	print(link.attr('href'))
parser.close()
```

## LICENSE

[MIT](http://www.opensource.org/licenses/mit-license.php)