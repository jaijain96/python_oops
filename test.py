"""
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def pre_order(node: Node):
    if node is None:
        return
    
    print(node.data)
    pre_order(node.left)
    pre_order(node.right)


root = Node(5)
root.left = Node(6)
root.right = Node(7)

pre_order(root)

from queue import Queue

q = Queue()
q.put(1)
q.put(3)
q.put(5)
q.put(7)
print(q.get())
print(q.get())


mat = [
    [1,1,0,0],
    [0,1,0,1],
    [0,1,1,1]
]


def dfs(row, col):
    if row < 0 or row >= n or col < 0 or col >= m or visited[row][col]:
        return
    
    visited[row][col] = True
    print(mat[row][col])
    # up
    dfs(row - 1, col)
    #right
    dfs(row, col + 1)
    # down
    dfs(row + 1, col)
    # left
    dfs(row, col - 1)


n = 3
m = 4

visited = [[False]*m]*n
print(visited)

dfs(0, 0)
