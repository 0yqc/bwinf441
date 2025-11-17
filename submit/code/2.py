alphabet = {
	'A': 0,
	'B': 1,
	'C': 2,
	'D': 3,
	'E': 4,
	'F': 5,
	'G': 6,
	'H': 7,
	'I': 8,
	'J': 9,
	'K': 10,
	'L': 11,
	'M': 12,
	'N': 13,
	'O': 14,
	'P': 15,
}
gpos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def explore(bars: int, figs: list[dict[str, str | int]], pos: list[int]) -> list[tuple[dict[str, str | int]]]:
	choreos = []
	for fig in figs:
		rem = bars
		rem -= fig['bars']
		if rem == 0:
			if apply_fig(pos, fig['pos_alph']) == gpos:
				choreos.append((fig,))
		elif rem < 0:
			continue
		else:
			pos = apply_fig(pos, fig['pos_alph'])
			ret = explore(rem, figs, pos)
			for choreo in ret:
				choreos.append((fig, *choreo))
	return choreos


def apply_fig(pos: list[int], fig: str) -> list[int]:
	new_pos = []
	for char in fig:
		new_pos.append(pos[alphabet[char]])
	return new_pos

def calc_distance(fig: str) -> int:
	distance = 0
	for i, char in enumerate(fig):
		distance += abs(alphabet[char] - i)
	return distance
	

with open('./inp/choreo06.txt', 'r') as f:
	bars = int(f.readline().strip())
	figs = []
	for _ in range(int(f.readline().strip())):
		raw = f.readline().strip().split(' ')
		figs.append({'name': raw[0], 'bars': int(raw[1]), 'pos_alph': raw[2]})

choreos = explore(bars, figs, gpos)

if not choreos:
	print('No valid choreo found.')
	exit()

high = {
	'max_dif': [0, None],
	'max': [0, None],
	'min': [float('inf'), None],
	'max_dis': [0, None],
	'min_dis': [float('inf'), None],
}

for choreo in choreos:
	figs = []
	n_dif = 0
	n_figs = 0
	dis = 0
	for fig in choreo:
		dis += calc_distance(fig['pos_alph'])
		n_figs += 1
		if not fig['name'] in figs:
			figs.append(fig['name'])
			n_dif += 1
	if n_dif > high['max_dif'][0]:
		high['max_dif'] = [n_dif, choreo]
	if n_figs > high['max'][0]:
		high['max'] = [n_figs, choreo]
	if n_figs < high['min'][0]:
		high['min'] = [n_figs, choreo]
	if dis > high['max_dis'][0]:
		high['max_dis'] = [dis, choreo]
	if dis < high['min_dis'][0]:
		high['min_dis'] = [dis, choreo]

print(f'Maximum different figures: 		{high['max_dif'][0]}: {', '.join([choreo['name'] for choreo in high['max_dif'][1]])}')
print(f'Maximum figures: 			{high['max'][0]}: {', '.join([choreo['name'] for choreo in high['max'][1]])}')
print(f'Minimum figures: 			{high['min'][0]}: {', '.join([choreo['name'] for choreo in high['min'][1]])}')
print(f'Maximum distance: 			{high['max_dis'][0]}: {', '.join([choreo['name'] for choreo in high['max_dis'][1]])}')
print(f'Minimum distance: 			{high['min_dis'][0]}: {', '.join([choreo['name'] for choreo in high['min_dis'][1]])}')
