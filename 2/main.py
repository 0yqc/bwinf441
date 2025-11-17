with open('./inp/choreo01.txt', 'r') as f:
	bars = int(f.readline().strip())
	figs = []
	for _ in range(int(f.readline().strip())):
		raw = f.readline().split(' ')
		figs.append({'name': raw[0], 'bars': int(raw[1]), 'pos_alph': raw[2]})

def explore(bars: int, figs: list[dict[str, str | int]]) -> list[dict[str, str | int]]:
	choreos = []
	for fig in figs:
		bars -= fig['bars']
		if bars == 0:
			choreos.append(fig)
		elif bars < 0:
			continue
		else:
			ret = explore(bars, figs)
			for choreo in ret:
				choreos.append(choreo)
	return choreos

print(explore(bars, figs))