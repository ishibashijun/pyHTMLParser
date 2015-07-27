pyHTMLParser
=========

### jQuery like HTML parser

## Usage
```python
parser = pyHTMLParser()
parser.open('http://www.example.com')
links = parser.tag('a')
for link in links:
	print(link.attr('href'))
parser.close()
```

## LICENSE

[MIT](http://www.opensource.org/licenses/mit-license.php)