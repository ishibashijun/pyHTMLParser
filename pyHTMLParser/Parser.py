# Copyright (c) 2015 Jun Ishibashi
#
# Permission is hereby granted, free of charge, to any person 
# obtaining a copy of this software and associated documentation 
# files (the "Software"), to deal in the Software without 
# restriction, including without limitation the rights to use, 
# copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the 
# Software is furnished to do so, subject to the following 
# conditions:
#
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
# OR OTHER DEALINGS IN THE SOFTWARE.

from urllib.request import *
from html.parser import HTMLParser
import re

from pyHTMLParser.pyNodeList import pyNodeList
from pyHTMLParser.pyNode import pyNode

def url_checker(url):
    result = re.match('^http[s]?://', url)
    if result is None: return False
    else: return True

SELF_CLOSING_TAG = ['area', 'base', 'br', 'col', 'command',
                    'embed', 'hr', 'img', 'input', 'keygen',
                    'link', 'meta', 'param', 'source', 'track',
                    'wbr']

def is_self_closing(tag):
    return tag in SELF_CLOSING_TAG
    
class Parser(HTMLParser):

    def __init__(self, url=None):
        super(self.__class__, self).__init__()
        if url is not None:
            if not url_checker(url):
                raise ValueError('Url must start with http:// or https://')
            else:
                self._url = url
        else:
            self._url = None
        self._dom = []
        self._nodes = pyNodeList()
        self._is_started = False
        self._decoder = 'utf-8'

    def set_decoding(self, dec):
        self._decoder = dec

    def open(self, url=None):
        if url is not None:
            if not url_checker(url):
                raise ValueError('Url must start with http:// or https://')
            else:
                self._url = url
        else:
            if self._url is None:
                raise ValueError('Url is empty')
        try:
            res = urlopen(self._url)
        except Exception:
            raise Exception('Error connecting at %s' % self._url)
        self._html = res.read().decode(self._decoder)
        res.close()
        self.feed(self._html)

    def close(self):
        super(self.__class__, self).close()
        self._html = ''
        self._url = None
        self._nodes = pyNodeList()
        del self._dom[:]

    def raw_html(self):
        return self._html

    def tag(self, tag):
        ret = pyNodeList()
        for node in self._nodes:
            if node.name() == tag.lower():
                ret.append(node)
        return ret

    def body(self):
        return self._nodes[0]

    def id(self, i):
        return self._nodes.id(i)

    def cls(self, c):
        return self._nodes.cls(c)

    def handle_starttag(self, tag, attrs):
        if not self._is_started:
            if tag.lower() == 'body':
                node = pyNode('body')
                self._is_started = True
                self._dom.append(node)
                self._nodes.append(node)
                for attr in attrs:
                    node.set_attr(attr[0], attr[1])
        else:
            node = pyNode(tag.lower())
            node.set_parent(self._dom[-1])
            self._dom[-1].add_child(node)
            if not is_self_closing(tag.lower()):
                self._dom.append(node)
            self._nodes.append(node)
            for attr in attrs:
                node.set_attr(attr[0], attr[1])
                    
    def handle_endtag(self, tag):
        if self._is_started:
            if tag == 'body':
                self._is_started = False
                self._dom.pop()
                assert len(self._dom) == 0, 'dom stack is not empty'
            else:
                end_node = self._dom.pop()
                end_node.parent()._children.extend(end_node.children())
                assert len(self._dom) != 0, 'dom stack is empty but parsing has not ended'

    def handle_startendtag(self, tag, attrs):
        if self._is_started:
            node = pyNode(tag.lower())
            node.set_parent(self._dom[-1])
            self._nodes.append(node)
            for attr in attrs:
                node.set_attr(attr[0], attr[1])

    def handle_data(self, data):
        if self._is_started: self._dom[-1].set_text(data)
            
if __name__ == '__main__':
    parser = pyHTMLParser.Parser()
    parser.open('http://www.example.com')
    links = parser.tag('a')
    for link in links:
        print(link.attr('href'))
    parser.close()
