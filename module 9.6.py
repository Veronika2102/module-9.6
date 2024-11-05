from itertools import combinations
def all_variants(text):
    tex = []
    for i in range(1, len(text)+1):
        tex = []
        b = combinations(text, i)
        tex.extend(b)
        for t in tex:
            t = list(t)
            yield (''.join(t))


a = all_variants("abc")
for i in a:
    if i == 'ac':
        continue
    print(i)

