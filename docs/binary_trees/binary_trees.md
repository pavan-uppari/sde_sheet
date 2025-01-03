## Inorder Traversal

```py
{!17_binary_tree/01_inorder.py!}
```

Links: [LC](https://leetcode.com/problems/binary-tree-inorder-traversal/)<br>

---

## Preorder Traversal

```py
{!17_binary_tree/02_preorder.py!}
```

Links: [LC](https://leetcode.com/problems/binary-tree-preorder-traversal/)<br>

---

## Postorder Traversal

```py
{!17_binary_tree/03_postorder.py!}
```

Links: [LC](https://leetcode.com/problems/binary-tree-postorder-traversal/)<br>

---

## LeftView Of Binary Tree

**Example**:  
Input: root[] = [1, 2, 3, 4, 5, N, N]

![alternate](https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/876845/Web/Other/blobid0_1731456264.png)

Output: [1, 2, 4]

Explanation: From the left side of the tree, only the nodes 1, 2, and 4 are visible.

**Algorithm**:  
Use BFS, result is list of first element in each level of binary tree.

```py
{!17_binary_tree/06_left_view.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/right-left-view-of-binary-tree/) [GFG](https://www.geeksforgeeks.org/problems/left-view-of-binary-tree/1)<br>

---

## Bottom View of Binary Tree

**Example**:  
![alternate](https://media.geeksforgeeks.org/img-practice/prod/addEditProblem/876845/Web/Other/blobid0_1731456264.png)

For the above tree, the output should be 4 2 5 3.

**Algorithm**:  
1. Use BFS, carry level during traversal, on going left decrease the level, on going right increase the level.  
2. Result is list of last elements in each level.  

```py
{!17_binary_tree/07_bottom_view.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/bottom-view-of-a-binary-tree/) [GFG](https://www.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1)<br>

---

## Top View of Binary Tree

**Algorithm**:  
Same as bottom view, result is list of first elements in each level. 

```py
{!17_binary_tree/08_top_view.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/top-view-of-a-binary-tree/) [GFG](https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1)<br>

---

## Vertical order traversal

**Problem Statement**: The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.  

**Example**:  
![img](https://assets.leetcode.com/uploads/2021/01/29/vtree2.jpg)

Input: root = [1,2,3,4,5,6,7]
Output: [[4],[2],[1,5,6],[3],[7]]

**Algorithm**:  
1. Use BFS, use level logic, on going left decrease the level, on going right increase the level.  
2. During BFS, we will be iterating for each height.  
3. If multiple elements found in the same level and also at the same height, sort them.  

```py
{!17_binary_tree/10_vertical_order.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/vertical-order-traversal-of-binary-tree/) [LC](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/)<br>

---

## Root to Leaf Paths

**Problem Statement**: Given a Binary Tree, you need to find all the possible paths from the root node to all the leaf nodes of the binary tree.

**Example**:  

Input: root[] = [1, 2, 3, 4, 5]

![alternate](https://media.geeksforgeeks.org/wp-content/uploads/20241007105251989873/ex-3.webp)

Output: [[1, 2, 4], [1, 2, 5], [1, 3]]   
Explanation: All possible paths: 1->2->4, 1->2->5 and 1->3

**Algorithm**:  
Use DFS

```py
{!17_binary_tree/11_root_to_node_path.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/print-root-to-node-path-in-a-binary-tree/) [GFG](https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1)<br>

---

## Max width of a Binary Tree

**Problem Statement**: Given a Binary Tree, return its maximum width. The maximum width of a Binary Tree is the maximum diameter among all its levels. The width or diameter of a level is the number of nodes between the leftmost and rightmost nodes.

**Example**:  

![alternate](https://assets.leetcode.com/uploads/2022/03/14/maximum-width-of-binary-tree-v3.jpg)

Input: root = [1,3,2,5,null,null,9,6,null,7]  
Output: 7  
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).

**Algorithm**:  
1. Use BFS, use index for every element while traversal.  
2. If i is index of a node, its left child index is 2*i, right child index is 2*i + 1.  
3. Find width at each level of BFS.  

```py
{!17_binary_tree/12_max_width.py!}
```

Links: [TUF](https://takeuforward.org/data-structure/maximum-width-of-a-binary-tree/) [LC](https://leetcode.com/problems/maximum-width-of-binary-tree/)<br>

---