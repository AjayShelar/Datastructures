class btree:
    def __init__(self, rootid):
        self.left = None
        self.right = None
        self.rootid = rootid

    def grc(self):
        return self.right
    def glc(self):
        return self.left
    def snv(self, value):
        self.rootid = value

    def gr(self):
        return self.rootid

    def ilc(self, new_node):
        if self.right == None:
            self.right = btree(new_node)
        else:
            tree = btree(new_node)
            self.right = tree
            tree = self.right

    def  irc(self, new_node):
        if self.left == None:
            self.left = btree(new_node)
        else :
            tree = btree(new_node)
            self.left = tree
            tree = self.left

    def display(self):
        print(gr())
        print(grc())
        print(glc())


#driver code

mytree = btree("ajay")
mytree.ilc("sanjay")
mytree.irc("shelar")
