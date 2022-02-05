from binarytree import Node



class Leaf(Node):
    def __init__(self, tag: str):
        super().__init__(tag)
        self.tag = tag
        self.parent = None
        self.right = None
        self.left = None

    def add_right(self, lf: "Leaf"):
        lf.parent = self
        self.right = lf

        return self

    def add_left(self, lf: "Leaf"):
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
            n = self.root_node()

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

    def width_dump(self):
        queue = [self]
        res = []

        while len(queue) >= 1:
            current = queue.pop(0)
            res.append(current)
            current_childs = (current.left or None, current.right or None)

            if current_childs != None:
                for child in current_childs:
                    if child is None:
                        continue
                    queue.append(child)

        for n in res:
            print(n.tag)

    def prefix_dump(self):
        print(self.tag)
        childs = (self.left or None, self.right or None)

        for child in childs:
            if child is None:
                continue
            child.prefix_dump()

    def suffix_dump(self):
        childs = (self.left, self.right)

        for child in childs:
            if child is None:
                continue
            child.suffix_dump()

        print(self.tag)

    def root_node(self):
        p = self
        while p.parent != None:
            p = p.parent

        return p


def tree_from_list(l: "Leaf", tags: "list[int]"):
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

def rotate_node_left(leaf: 'Leaf'):
    if leaf.right is not None:
        leaf.right.left = Leaf(leaf.tag)

    return leaf.right

