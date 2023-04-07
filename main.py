from bplustree import Bplustree
from utils import print_tree

print('Initializing B+ tree...')
order = int(input('Order of the B plus Tree => '))
tree = Bplustree(order)

while 1:
    x = int(input(
        'Enter 1 for Insert\n      2 for Delete\n      3 for Print tree\n      4 for searching a number\n      Any Other to Exit : '))
    if x == 1:
        p = int(input('Enter the Number to insert : '))
        tree.insert(p)
    elif x == 2:
        k = int(input('Enter the Number to delete : '))
        tree.delete(k)
    elif x == 3:
        print_tree(tree.root, '   ', 0)
    elif x==4:
        ans =tree.search(int(input('Enter the number to search for : ')),tree.root)
        if ans[2]==1:
            print('Number found')
            print('Index : ',ans[0])
            print('Node : ',ans[1].keys)
            print("number : ",ans[1].keys[ans[0]])
        else:
            print('Number not found')
    else:
        break
