class RootedTree:
    def __init__(self, value, children):
        self.value = value
        self.children = children

def DFS(tree, l):
    l.append(tree.value)
    if tree.children:
        for child_node in tree.children:
            DFS(child_node, l)

class BackTracker:
    def __init__(self, init_state, trans):
        self.trans = trans
        self.stack = [{ "state": init_state, "next": trans(init_state), "i": 0 }]
    
    def cur_state(self):
        return self.stack[-1]["state"]
    
    def next_state(self):
        if len(self.stack) is 0:
            return None
        while self.stack[-1]["i"] >= len(self.stack[-1]["next"]):
            self.stack.pop()
            if len(self.stack) is 0:
                return None
            self.stack[-1]["i"] = self.stack[-1]["i"] + 1
        new_state = self.stack[-1]["next"][self.stack[-1]["i"]]
        self.stack.append({ "state": new_state, "next": self.trans(new_state), "i": 0 })
        return new_state

def bt_search(init_state, trans, isSuccess):
    searcher = BackTracker(init_state, trans)
    while not isSuccess(searcher.cur_state()):
        if searcher.next_state() is None:
            return None
    return searcher.cur_state()

class SudokuState:
    def __init__(self, board):
        self.board = [item for sublist in board for item in sublist]
        self.filled = [x is not 0 for x in self.board]
        self.target = self.filled.index(False) if False in self.filled else None
	
    def numSet(self, indicies):
        return set([self.board[k] for k in indicies if self.filled[k]])
    
    def findCandidates(self):
        if self.target is None:
            return []
        row = self.target // 9
        col = self.target % 9
        regR = (row//3)*3
        regC = (col//3)*3
        rowSet = self.numSet([9*row+i for i in range(9)])
        colSet = self.numSet([9*j+col for j in range(9)])
        regSet = self.numSet([9*(regR+j)+(regC+i) for i in range(3) for j in range(3)])
        return set(range(1,10)) - (rowSet | colSet | regSet)
	
	def genNext(self):
        k = self.target
        res = []
        for n in self.findCandidates():
            newState = deepcopy(self)
            newState.board[k] = n
            newState.filled[k] = True
            newState.target = newState.filled.index(False) if False in newState.filled else None
            res.append(newState)
        return res

s1 = SudokuState([[0,0,4,0,0,0,0,8,0],
[1,0,0,3,0,2,4,0,0],
[2,0,0,5,0,0,0,1,6],
[0,0,7,0,0,6,0,9,1],
[4,0,9,0,0,0,5,0,2],
[6,5,0,1,0,0,7,0,0],
[7,4,0,0,0,8,0,0,5],
[0,0,1,2,0,5,0,0,9],
[0,8,0,0,0,0,1,0,0]])

temp = "\n".join(["   |   |   ",
"   |   |   ",
"   |   |   ",
"---+---+---",
"   |   |   ",
"   |   |   ",
"   |   |   ",
"---+---+---",
"   |   |   ",
"   |   |   ",
"   |   |   "])

def isSuccess(s): 
	return s.target is None 

def trans(s): 
	return s.genNext()

for i, c in enumerate(temp2): 
	if c is ' ': 
		temp2[i] = str(result.board[j]) 
		j = j + 1
