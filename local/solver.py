from cube import Cube
import random

def scramble(i,n,cube):
    c = [-1,1]
    for x in range(i):
        r1 = random.randint(0,2)
        r2 = random.randint(1,n)
        r3 = random.choice(c)
        cube.transform(r2,r1,r3)

def heuristic(cube):
    return 1
def move(n, index):
    n_val = index%n
    c_val = index//n
    a_val = c_val%3
    r_val = 1 if c_val//3 == 1 else -1
    return [n_val+1,a_val,r_val]
def push(open_list, node):
    for i in open_list:
        if(node['g_val'] + node['h_val'] == i[0]):
            if( node['h_val']<i[1]):
                open_list.insert((node['g_val'] + node['h_val'], node['h_val'],node), open_list.index(i))
                return
        elif(node['g_val'] + node['h_val'] < i[0]):
            open_list.insert((node['g_val'] + node['h_val'], node['h_val'],node), open_list.index(i))
            return
    open_list.append((node['g_val'] + node['h_val'], node['h_val'],node))
def pop(open_list):
    _, _, curr = open_list.pop()
    return curr
# basically a depth first search without a proper heuristic for now
# modified IDA* 
def IDAStar(cube, limit = -1, start = None):
    # limit set to an unreachable number by default
    # starting node
    if start == None:
        start = {
            "cube": cube,
            "g_val": 0,
            "transform": None,
            "parent": None,
            "h_val": heuristic()
        }
    successors = []
    nodeStack = []
    bound = 0
    nextBound = heuristic(cube)
    currCube = cube
    solved = False
    while not solved:
        # when nodestack is empty it means either it was just initialized or 
        # we return to the root after a branch doesnt have a solution within the bounds
        if len(nodeStack) == 0:
            bound = nextBound
            nextBound*=2
            nodeStack.append(start)
        # set the current nodes
        currNode = nodeStack.pop()
        currCube = currNode["cube"]
        # if it is bound check if the problem has been solved if it has then end 
        if currCube.solved():
            solved = True
        elif currNode["h_val"] < limit:
            solved = True
        # cannot be above bound by the nature of how elements were pushed
        if currNode["g_val"] != bound:
            # make all moves possible
            for i in range(2*3*cube.n):
                # create the states of the cubes
                m = move(cube.n,i)
                # trust that this is a deep copy otherwise it can lead to bugs
                copy = Cube(currNode["cube"].data, cube.n)
                # print(currNode['g_val'])
                copy.transform(m[0],m[1],m[2])
                node = {"cube": copy, "h_val": heuristic(cube), "g_val": \
                    currNode["g_val"] + 1, "transform": m}
                if(node["h_val"]+node["g_val"]<=bound):
                    # print(len(successors))
                    push(successors,node)
                elif(node["h_val"]+node["g_val"]<nextBound):
                    nextBound = node["h_val"]+node["g_val"]
            # I'm not sure if i should reverse this but reversing seems correct to me 
            # if it causes an error comment out or remove the reverse()
            successors.reverse()
            while(len(successors)!=0):
                tnode = pop(successors)
                node = {"cube": tnode["cube"],"g_val":tnode["g_val"],
                    "transform": tnode["transform"],"parent":currNode, "h_val": tnode["h_val"]}
                nodeStack.append(node)
    return currNode

# waiting on a proper heuristic
def pseudoThistle(cube):
    hLimit = heuristic(cube)*3/4
    currNode = None
    c1 = cube
    while(hLimit>5):
        if currNode!=None:
            c1 = currNode["cube"]
        currNode = IDAStar(c1, hLimit, currNode)
        hLimit*=3/4
    return IDAStar(currNode["cube"],-1,currNode)

# get the path 
def getPath(node):
    currNode = node
    path = []
    while currNode["transform"]!=None:
        path.append(currNode["transform"])
        currNode = currNode["parent"]
    path.reverse()
    return path

# testing purposes


# transform(1,1) turns front face
# transform(1,0) turns right face
# transform(1,2) turns bottom face
cube = Cube(None)
scramble(5,3,cube)
# cube.transform(1,1,-1)
# m = [1,0,-1]
print(getPath(IDAStar(cube)))
for i in range(18):
    print(move(3,i))
path = getPath(IDAStar(cube))
for i in path:
    cube.transform(i[0],i[1],i[2])

        



cube.draw3()


