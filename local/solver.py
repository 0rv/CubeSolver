from cube import Cube

#print("Hello world")

# for in (list of cube moves) - (path(last)):
# search new

dcube = Cube(None, 3)

dcube.transform(index=2, axis=0, dir=1)
#print(dcube)
dcube.transform(index=2, axis=1, dir=1)
#print(dcube)
dcube.transform(index=2, axis=2, dir=1)
print(dcube)




dcube.draw3()



pass