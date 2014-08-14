pyHTMLParser
=========

### jQuery like HTML parser

## Usage
```python
parser = pyHTMLParser()
parser.open('http://www.yahoo.co.jp')
imgs = parser.tag('img')
for img in imgs:
	print(img.attr('src'))
parser.close()
```

## LICENSE

[MIT](http://www.opensource.org/licenses/mit-license.php)