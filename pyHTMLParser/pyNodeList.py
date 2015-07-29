class pyNodeList(list):

    def __init__(self):
        super(self.__class__, self).__init__()

    def first(self):
        return self[0]

    def last(self):
        return self[-1]

    def eq(self, index):
        if index < 0 and len(self) > abs(index):
            return self[index]
        elif index >= 0 and index < len(self):
            return self[index]
        return None

    def even(self):
        ret = pyNodeList()
        is_even = False
        for i in range(len(self)):
            if is_even: ret.append(self[i])
            is_even = not is_even
        return ret

    def odd(self):
        ret = pyNodeList()
        is_odd = True
        for i in range(len(self)):
            if is_odd: ret.append(self[i])
            is_odd = not is_odd
        return ret

    def gt(self, index):
        return self[index:]

    def lt(self, index):
        return self[:index]

    def id(self, i):
        for node in self:
            if node.get_attr('id') == i:
                return node
        return None

    def cls(self, c):
        ret = pyNodeList()
        for node in self:
            n = node.attr('class')
            if 'class' in self._attr and node.attr('class').find(c) is not -1:
                ret.append(node)
        return ret

    def contains(self, text):
        ret = pyNodeList()
        for node in self:
            if node.text().find(text) is not -1:
                ret.append(node)
        return ret
