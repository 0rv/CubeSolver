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
    pass
def move(n, index):
    # TODO find a way to optumize this later
    # theres probably a better way to do this cause this just seems slow 
    movement = []
    c = [-1,1]
    for i in range(1,n+1):
        for j in range(0,3):
            for k in c:
                movement.append([i,j,k])
    return movement[index]
def push(node):
    # TODO make this function
    pass
def pop():
    # TODO make this function
    pass
def IDAStar(cube):
    # starting node
    start = {
        "cube": cube,
        "g_val": 0,
        "transform": None,
        "parent": None
    }
    successors = []
    nodeStack = []
    bound = 0
    nextBound = heuristic(cube)
    currCube = cube
    while not currCube.solved():
        if len(nodeStack) == 0:
            bound = nextBound
            nextBound*=2
            nodeStack.append(start)
        currNode = nodeStack.pop()
        currCube = currNode["cube"]
        if currNode["g_val"] != bound:
            for i in range(2*3*cube.n):
                m = move(cube.n,i)
                copy = Cube(currNode["cube"])
                copy.transform(m[0],m[1],m[2])
                node = {"cube": copy, "h_val": heuristic(cube), "g_val": \
                    currNode["g_val"] + 1, "transform": m}
                if(node["h_val"]+node["g_val"]<=bound):
                    push(node)
                elif(node["h_val"]+node["g_val"]<nextBound):
                    nextBound = node["h_val"]+node["g_val"]
        # I honestly dont know if this is right but it seems right to me
        # Theres a chance that the first while loop will cause a bug
        temp = 0
        while(len(successors)!=0):
            temp = []
            temp.append(pop())
        while(len(temp)!=0):
            tnode = temp.pop()
            node = {"cube": tnode["cube"],"g_val":tnode["g_val"],
                "transform": tnode["transform"],"parent":currNode}
            nodeStack.append(node)
    return currNode

# get the path 
def getPath(node):
    currNode = node
    path = []
    temp = []
    while currNode["transform"]!=None:
        temp.append(currNode["transform"])
        currNode = currNode["parent"]
    while len(temp)!=0:
        path.append(temp.pop())
    return path

        
# transform(1,1) turns front face
# transform(1,0) turns right face
# transform(1,2) turns bottom face
cube = Cube(None)
scramble(20,3,cube)
# cube.transform(1,1,-1)




        



cube.draw3()


