from cube import Cube

def heuristicFunction(heuristicFunc,cubeState,weight=1):
    return weight*heuristicFunc(cubeState)

def exampleHeuristic(cubeState):
    #We have cuube
    #We must see how close we are to solving the cuube
    #But we have no function
    return 1

def purityHeur(inputCube):
    faceDict = []
    faces = [
    (0),
    (slice(None), 0),
    (slice(None), slice(None), 0),
    (inputCube.n+1),
    (slice(None), inputCube.n+1),
    (slice(None), slice(None), inputCube.n+1),
      ]
    for face, i in zip(faces, [1, 2, 3, 4, 5, 6]):
        realFace = inputCube.data[face]
        faceList = [0,0,0,0,0,0] # Count each color on this face
        for hori in realFace[1:-1]:
            for surf in hori[1:-1]:
                faceList[surf-1] = faceList[surf-1] + 1
        faceDict.append(faceList)
    # Find most pure side
    # Find max
    maxim = [[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]] # Sub is face, First is the amount, the second is the color
    while -1 in [takenFace[0] for takenFace in maxim]:
        for face in range(6): # for each face
            for color in range(6):
                possible = faceDict[face][color]
                if possible > maxim[face][0]:
                    # We should check if anything else has a claim, or rather, a better claim
                    success = True
                    for x in range(6): # We check all maxim for color
                        if x == face: # We're not looking at our current face tho
                            continue
                        elif maxim[x][1] == color: #Different face, same color!
                            if maxim[x][0] < possible: # If it sucks, we'll replace
                                maxim[x] = [-1,-1]
                            else: # If it's good, we're not going to do our own replace then
                                success = False
                                continue
                    if success == True:
                        maxim[face] = [possible,color]
    totalHeur = 0.0
    sizeN = (len(inputCube.data)-2)**2
    for face in maxim:
        totalHeur = totalHeur + (sizeN-face[0])
    return totalHeur
