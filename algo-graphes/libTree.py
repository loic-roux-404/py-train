class Leaf:
    def __init__(self, tag: str):
        self.tag = tag
        self.parent = None
        self.right = None
        self.left = None

    def add_right(self, lf: 'Leaf'):
        lf.parent = self
        self.right = lf

        return self

    def add_left(self, lf: 'Leaf'):
        lf.parent = self
        self.left = lf

        return self

    def _search(self, tag):
        if tag == self.tag:
            return True

        if self.right is not None and self.right.tag > tag:
            if self.left is not None:
                return self.left._search(tag)

        if self.left is not None and self.left.tag > tag:
            if self.right is not None:
                return self.right._search(tag)

        return False

    def search(self, tag):
        n = self
        if n.parent != None:
            n = self.genesis_node()

        return n._search(tag)

    def dump(self):
        print(self.tag)
        if self.left != None:
            self.left.dump()
        if self.right != None:
            self.right.dump()

    def infix_dump(self):
        if self.left != None:
            self.left.infix_dump()

        print(self.tag)

        if self.right != None:
            self.right.infix_dump()

    def genesis_node(self):
        p = self
        while p.parent != None:
            p = p.parent

        return p

def tree_from_list(l: 'Leaf', tags: 'list[int]'):
    if len(tags) == 0:
        return l

    if l is None:
        l = Leaf(tags.pop(0))

    if len(tags) >= 1:
        l.add_left(Leaf(tags.pop(0)))
        tree_from_list(l.left, tags)

    if len(tags) >= 1:
        l.add_right(Leaf(tags.pop(0)))
        tree_from_list(l.right, tags)

    return l
