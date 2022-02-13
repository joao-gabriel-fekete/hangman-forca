animationPath = ['animationFile\drawing0.txt','animationFile\drawing1.txt','animationFile\drawing2.txt','animationFile\drawing3.txt','animationFile\drawing4.txt','animationFile\drawing5.txt','animationFile\drawing6.txt']


def animation(x):
    global animationPath
    collection = []
    for i in animationPath:
        with open(i, 'r') as f:
            collection.append(f.read())

    targeted = collection[x]

    print(targeted) 


