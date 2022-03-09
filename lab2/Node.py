# Создадим класс Node, чтобы осуществить поиск через бинарное дерево.
# Создадим корневой узел
class Node:
    def __init__(self, data, index):
        self.data = data
        self.index = index
        self.left = None
        self.right = None


# Сортировка дерева
def inorder(root):
    if root is not None:
        # Обход левого поддерева
        inorder(root.left)
        # Обход корня
        print(str(root.data) + " ", end=' ')
        # Обход правого поддерева
        inorder(root.right)

# Вставка элемента
def insert(node, data, index):
    # Если дерево пустое, вернём новый узел
    if node is None:
        return Node(data, index)
    # Переход в левое или правое поддерево и вставка узла
    if data < node.data:
        node.left = insert(node.left, data, index)
    else:
        node.right = insert(node.right, data, index)
    return node

# Поиск inorder-преемника
def minValueNode(node):
    current = node
    # Inorder-преемник - это найденный крайний левый лист
    while(current.left is not None):
        current = current.left
    return current