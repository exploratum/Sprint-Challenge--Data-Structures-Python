import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

###########################################################################
# Binary Tree Search solution (insertion complexity: O(h(eight of tree)), 
# comparison: n * O(h(eight of tree))
###########################################################################

# Setup binary tree and insert all names of names_1
bst = BinarySearchTree(names_1[0])

for i in range(1,len(names_1)):
    bst.insert(names_1[i])

# look up for duplicates
duplicates=[]
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

#####################################
# Original solution (runtime: 5.5 s.)
# complexity: O(n**2)
######################################
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

######## ############################## STRETCH ###################################
# STRETCH - only Python lists - No extra storage for binary tree  (runtime: 1.11 s.)
####################################################################################
# 
# duplicates = [name for name in names_1 if name in names_2]

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

