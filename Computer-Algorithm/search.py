class TreeNode:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

def insert(node, key):
    # node는 부모 노드이다.
    if node == None:## 부모가 Null이면
        node = TreeNode(key)
        return node
    else:
        if (key < node.key):
            node.left = insert(node.left, key)
        elif (key > node.key):
            node.right = insert(node.right, key)
        else:
            return node
    return node

def inorder(root):
    ## LVR : 중위 순회 (오름차순으로 노드의 값을 정렬해서 반환하는 것이 가능하다.)
    if (root == None):
        return
    inorder(root.left)
    print(root.key, end = ' ')
    inorder(root.right)

def searchNode(root, key):
    if (root == None):
        return None
    if (key == root.key):
        return root
    elif (key < root.key):
        return searchNode(root.left, key)
    else:
        return searchNode(root.right, key)

def getHeight(node):
    height = 0
    if (node != None):
        height = 1 + max(getHeight(node.left), getHeight(node.right))
    return height

def getBalance(node):
    if (node == None):
        return 0;
    return getHeight(node.left) - getHeight(node.right) ## left - right > 1 : L / left - right < -1 : R

def insertAVL(node, key):
    def rotateRight(node):
        temp = node.left
        node.left = temp.right
        temp.right = node
        return temp
    def rotateLeft(node):
        temp = node.right
        node.right = temp.left
        temp.left = node
        return temp
    if node == None:
        return TreeNode(key)
    if (key < node.key):
        node.left = insertAVL(node.left, key)
    elif (key > node.key):
        node.right = insertAVL(node.right, key)
    else:return node
    balance = getBalance(node)
    if (balance > 1 and key < node.left.key): ## LL
        return rotateRight(node)
    if (balance <-1 and key > node.right.key): ## RR
        return rotateLeft(node)
    ## 여기부터는 2차례의 회전을 해야 한다.
    if (balance > 1 and key > node.left.key): ## LR
        node.left = rotateLeft(node.left)
        return rotateRight(node)
    if (balance < -1 and key < node.right.key): ## RL
        node.right = rotateRight(node.right)
        return rotateLeft(node)
    return node



def preorder(root):
    if (root == None):
        return
    print(root.key, end = ' ')
    preorder(root.left)
    preorder(root.right)

if __name__ == "__main__":
    root = None ## rootnode
    rootAVL = None
    keys = [35, 25, 13, 40,45]
    for key in keys:
        root = insert(root, key)
    #preorder(root)
    print()
    for key in keys:
        rootAVL = insertAVL(rootAVL, key) ## 균형이 잡히도록
        preorder(rootAVL)
        print()
    preorder(rootAVL)

    """
    inorder(root)
    searchN = 30
    search = searchNode(root,searchN)
    print(" ")
    if search!=None:
        print("Found " + str(searchN))
    else:
        print("Not Found " + str(searchN))
    """