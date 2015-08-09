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

from pyHTMLParser.pyNodeList import pyNodeList

class pyNode:

    def __init__(self, name=None):
        self._name = name
        self._attr = {}
        self._html = ''
        self._text = ''
        self._parent = None
        self._children = pyNodeList()

    def __str__(self):
        return self._name

    def name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def is_null(self):
        return True if self._name is None else False

    def set_attr(self, key, value):
        if not key in self._attr: self._attr[key] = value
        else: self._attr[key] += ' ' + value

    def attr(self, key):
        if not key in self._attr: return None
        else: return self._attr[key]

    def id(self):
        return self._attr['id'] if 'id' in self._attr else None

    def cls(self):
        if 'class' in self._attr: return self._attr['class']
        else: return None

    def has_class(self, cls):
        if 'class' in self._attr:
            return self._attr['class'].find(cls) is not -1
        return False

    def html(self):
        if self._html is not '': return self._html
        self._html += '<'+self.name()
        for attr in self._attr:
            self._html += ' '+attr+'="'+self._attr[attr]+'"'
        self._html += '>'+self._text
        if not is_self_closing(self.name()):
            if self.has_child:
                for ch in self.children():
                    self._html += ch.html()
            self._html += '</'+self.name()+'>'
        return self._html

    def set_html(self, html):
        self._html = html

    def text(self):
        return self._text

    def set_text(self, text):
        self._text = text

    def has_parent(self):
        return False if self._parent is None else True

    def set_parent(self, parent):
        self._parent = parent

    def parent(self):
        return self._parent

    def parents(self):
        ret = pyNodeList()
        par = self._parent
        ret.append(par)
        while par.has_parent():
            par = par._parent
            ret.append(par)
        return ret

    def has_child(self):
        return len(self._children) is not 0

    def add_child(self, child):
        self._children.append(child)

    def children(self):
        return self._children

    def child(self, child_tag=None):
        if childTag is None: return self._children
        ret = pyNodeList()
        for node in self._children:
            if node.name() == childTag:
                ret.append(node)
        return ret

    def next_all(self):
        ret = pyNodeList()
        if self.has_parent():
            brothers = self._parent.children()
            pass_me = False
            for i in range(len(brothers)):
                bro = brothers[i]
                if pass_me: ret.append(bro)
                if bro is self: pass_me = True
        return ret

    def prev_all(self):
        ret = pyNodeList()
        if self.has_parent():
            brothers = self._parent.children()
            for i in range(len(brothers)):
                bro = brothers[i]
                if bro is self: break
                ret.append(bro)
        return ret