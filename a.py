import itertools
N=2
move=[[1,0],[-1,0],[0,1],[0,-1]]
start=[0,0]
Goal=[1,1]
mp={}

for movelist in itertools.combinations_with_replacement(move,2):
    log1=[[0,0]]
    now=[0,0]
    for i,x in enumerate(movelist):
        print(i,log1)
        now[0]+=x[0]
        now[1]+=x[1]
#         print(tuple(log),now)
        print(now)
    
        log1.append(now)
#         print(tuple(log1),now)
        print(log1)
    break
    print('t')
