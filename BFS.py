def RemoveDeadPath(goal,path,Graph):
    PreviousNode=goal
    for i in reversed(range(len(path[:-1]))):
        if PreviousNode not in Graph[path[i]]:
            path.pop(i)
        PreviousNode=path[i]
    return path

def BreadthFirstSearch(Goal,start ,Graph):
    stack,path=[],[]
    found=False
    stack.append(start)
    while stack:
        x=stack[0]
        stack.pop(0)
        path.append(x)
        if Goal==x:
            found=True
            break
        for child in Graph[x]:
            stack.append(child)
    if found:
        print("path =",path)
    else:
        print("Not exist!")

Graph={
'A':['B','C'],
'B':['D','E'],
'C':['F'],
'D':[],
'E':[],
'F':[]
}


BreadthFirstSearch('F','A',Graph)





