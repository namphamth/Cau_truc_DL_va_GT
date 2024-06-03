class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def duyet_cay_giua(root):
    if root != None :
        # Duyệt cây con bên trái
        duyet_cay_giua(root.left)
        
        # In giá trị của nút hiện tại
        print(root.val, end=" ")

        # Duyệt cây con bên phải
        duyet_cay_giua(root.right)

# Sử dụng

root = Node(1)
root.right = Node(2)
root.right.left = Node(3)

print("Duyet cay theo thu tu giua:")
duyet_cay_giua(root)
