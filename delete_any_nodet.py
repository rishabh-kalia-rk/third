# deletethe node
# that node may have no child, one child, two child

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def create(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        return Node(data)

    def insert(self, data, node):
        if node is None:
            return self.create(data)
        if data < node.data:
            node.left = self.insert(data, node.left)
        else:
            node.right = self.insert(data, node.right)
        return node


# --------delete any node but not for root node deletion --------------


    def delete_element(self, node, data):
        if self.root is None:
            print("tree is empty")
            return

        if data < node.data:
            if node.left:
                # if not None than execute if. means if left child present
                node.left = self.delete_element(node.left, data)
                # this is to call delete again and now node is at node.left reference after the delete called.
            else:
                print("node not present")

        elif data > node.data:
            if node.right:
                # if not None than execute if. means if left child present
                node.right = self.delete_element(node.right, data)
            else:
                print("node not present")

        else:
            # this execute when node.data=data
            # means we found the node
            if node.left is None and node.right is None:
                # this means we are at root node and node has no child
                if count_node(node) == 1 and node.data == data:
                    # means if only root node is present
                    print("can't delete as tree will be empty after this")

                temp = node.right
                node = None
                return temp
            elif node.left is not None and node.right is None:
                # if node is root node
                temp = node.left
                if node.data == data and count_node(node) == 2:
                    node.data = node.left.data
                    node.left = temp.left
                    node.right = temp.right
                    temp = None
                    return node

                # node has one left child

                node = None
                return temp

            elif node.left is None and node.right is not None:
                # node has one right child
                temp = node.right
                if node.data == data and count_node(node) == 2:
                    node.data = node.right.data
                    node.right = temp.right
                    node.left = temp.left
                    temp = None
                    return node
                node = None
                return temp

            else:
                x = node.right
                while x.left:
                    # while execute until left child is none. here we want to find smallest element in right subtree
                    # as smallest element will be in left branch of subtree so we are traversing in left branch.
                    x = x.left
                    # as leaf node will be the least value if present.
                # this replace the data of node to be deleted with data of smallest node.
                node.data = x.data
                # one we find the smallest element we call the delete method to delete now duplicate value of smalled data in subtree.
                node.right = self.delete_element(node.right, x.data)
                # bz we want to delete node in right subtree so we send node.right.

        return node


# -------------print tree------------------

    def print_inorder(self, cur_node, traversal):
        ''' node is the reference of root node self.root'''
        if cur_node is not None:
            traversal = self.print_inorder(cur_node.left, traversal)
            traversal += (str(cur_node.data) + "-")
            traversal = self.print_inorder(cur_node.right, traversal)
        return traversal

    def level(self, node):
        q = []
        i = 0
        k = 0

        q.append(node)
        while len(q) != 0:
            node = q.pop(0)
            if i == 2**k:
                k += 1
                i = 0
                print("")
            if node == "None":
                print("N", end=' ')
                i += 1
                q.append("None")
                q.append("None")

                continue
            root = node.data

            print(root, end=' ')
            i += 1
            if node.left is not None:
                q.append(node.left)
            else:
                q.append("None")
            if node.right is not None:
                q.append(node.right)
            else:

                q.append("None")

            if self.all_same(q):
                if i != 2**k:
                    while i != 2**k:
                        print("N", end=" ")
                        i += 1
                print(" ")
                break

    def all_same(self, items):
        return all(x == "None" for x in items)

# ----------function to find no of node in tree---------


def count_node(node):
    if node is None:
        return 0
    return count_node(node.left)+count_node(node.right)+1


tree = BST()
tree.create(16)
n = tree.root
tree.insert(27, n)
tree.insert(13, n)
tree.insert(11, n)
tree.insert(28, n)
# tree.insert(24, n)
# tree.insert(30, n)
# tree.insert(33, n)
# tree.insert(29, n)
# tree.insert(10, n)
# tree.insert(17, n)
# tree.insert(14, n)
# tree.insert(15, n)
# tree.insert(13.5, n)

# tree.insert(12, n)
tree.level(n)
# tree.delete_element(n, 13)
tree.delete_element(n, 16)
tree.level(n)
print("\n", tree.print_inorder(n, ""))
