states = [(i,j) for i in range(3) for j in range(3)]
actions = ['up','down','left','right']
goal, obstacle, gamma = (2,2), (1,1), 0.9

def step(s,a):
    if s == goal: return s
    i,j = s
    moves = {'up':(i-1,j),'down':(i+1,j),'left':(i,j-1),'right':(i,j+1)}
    ns = moves[a]
    return ns if 0<=ns[0]<3 and 0<=ns[1]<3 and ns!=obstacle else s
def reward(s,ns):
    return 10 if ns==goal else (-1 if s!=goal else 0)

V = {s:0 for s in states}

while True:
    delta = 0
    newV = V.copy()
    for s in states:
        if s == obstacle: continue
        newV[s] = max(reward(s,step(s,a)) + gamma*V[step(s,a)] for a in actions)
        delta = max(delta, abs(V[s]-newV[s]))
    V = newV
    if delta < 1e-3: break

print("Values:")
for i in range(3):
    print([round(V[(i,j)],2) for j in range(3)])
