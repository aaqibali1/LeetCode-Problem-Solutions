# creating trie
class TrieNode:
    def __init__(self):
        self.child = {}
        self.endWord = ""

    def insertWord(self, word): # method to add words in trie
        cur_node = self
        for c in word:
            if c not in cur_node.child:
                 cur_node.child[c] = TrieNode()
            cur_node = cur_node.child[c]
        cur_node.endWord = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode() #initialized root

        for word in words: #adding each word of words list to the trie
            root.insertWord(word)

        ans = set() # to keep final answers
        visited = set()  # to keep track of visited nodes during search   
        
        def search(m,n, node, w): # dfs on board to find words
          
            if (m < 0 or m >= len(board) or n < 0 or n >= len(board[0])
            or (m,n) in visited or board[m][n] not in node.child):                 
                 return

            visited.add((m,n)) #adding visited cells to the set                    
            node = node.child[board[m][n]]
            w = w + board[m][n]            
            

            search(m - 1, n, node , w)
            search(m + 1, n, node , w)
            search(m, n - 1, node , w)
            search(m, n + 1, node , w)

            if node.endWord != "": # checking if word exists                
                ans.add(w)
            visited.remove((m,n)) #removing visited cells from the set
            

        for r in range(len(board)):
            for c in range(len(board[0])):
                search(r, c, root, "")                   


        return ans  