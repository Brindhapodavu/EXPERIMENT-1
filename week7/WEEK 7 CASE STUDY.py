states = ['Interested', 'Neutral', 'Disengaged']

start = {'Interested': 0.5, 'Neutral': 0.3, 'Disengaged': 0.2}

trans = {
    'Interested': {'Interested': 0.6, 'Neutral': 0.3, 'Disengaged': 0.1},
    'Neutral': {'Interested': 0.2, 'Neutral': 0.5, 'Disengaged': 0.3},
    'Disengaged': {'Interested': 0.1, 'Neutral': 0.3, 'Disengaged': 0.6}
}

emit = {
    'Interested': {'click': 0.8, 'time': 0.2},
    'Neutral': {'click': 0.5, 'time': 0.5},
    'Disengaged': {'click': 0.2, 'time': 0.8}
}

obs = ['click', 'time']

alpha = {s: start[s] * emit[s][obs[0]] for s in states}

for o in obs[1:]:
    alpha = {
        s: sum(alpha[p] * trans[p][s] for p in states) * emit[s][o]
        for s in states
    }

print("Probability of observation sequence:", sum(alpha.values()))




 OUTPUT:

     Probability of observation sequence: 0.2455


