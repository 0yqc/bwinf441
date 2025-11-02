def main():
	with open('./inp/drehfreudig04.txt', 'r') as f:
		txt = f.read().strip()
	tree = eval(txt.replace(')', '),').strip(','))
	leafs = explore_leafs(tree)
	print('Drehfreudig!' if leafs == leafs[::-1] else 'Nicht drehfreudig.')
	csvg(tree, leafs)


def explore_leafs(tree: tuple[tuple | None], width: float = 1, depth: int = 0) -> tuple[tuple[float, int]]:
	if not tree:
		return ((width, depth),)
	else:
		leafs = []
		for node in tree:
			leafs.extend(explore_leafs(node, width / len(tree), depth + 1))
		return tuple(leafs)


def rcsvg(tree: tuple[tuple | None], width: float = 1, depth: int = 0, maxd: int = 0, pos: tuple[float, float] = (0, 0), ppos: tuple[float, float] | None = None) -> str:
	if tree:
		ts = f'''
		<circle cx="{pos[0] + width / 2}cm" cy="{pos[1] + .5}cm" r="0.0625cm" fill="#ff0000"></circle>
		<line x1="{pos[0]}cm" y1="{pos[1]}cm" x2="{pos[0] + width}cm" y2="{pos[1]}cm" stroke="#000000" strokewidth="0.03125cm"></line>
		<line x1="{pos[0]}cm" y1="{pos[1]}cm" x2="{pos[0]}cm" y2="{pos[1] + 1}cm" stroke="#000000" strokewidth="0.03125cm"></line>
		<line x1="{pos[0] + width}cm" y1="{pos[1]}cm" x2="{pos[0] + width}cm" y2="{pos[1] + 1}cm" stroke="#000000" strokewidth="0.03125cm"></line>
		'''.strip().replace('\n', '').replace('\t', '')
		xo = 0
		for node in tree:
			ts += rcsvg(node, width = width / len(tree), depth = depth + 1, maxd = maxd, pos = (pos[0] + xo, pos[1] + 1), ppos = (pos[0] + width / 2, pos[1] + .5))
			xo += width / len(tree)
	else:
		ts = f'''
		<circle cx="{pos[0] + width / 2}cm" cy="{pos[1] + .5}cm" r="0.0625cm" fill="#ff0000"></circle>
		<line x1="{pos[0]}cm" y1="{pos[1]}cm" x2="{pos[0] + width}cm" y2="{pos[1]}cm" stroke="#000000" strokewidth="0.03125cm"></line>
		<line x1="{pos[0]}cm" y1="{pos[1]}cm" x2="{pos[0]}cm" y2="{maxd + 1}cm" stroke="#000000" strokewidth="0.03125cm"></line>
		<line x1="{pos[0] + width}cm" y1="{pos[1]}cm" x2="{pos[0] + width}cm" y2="{maxd + 1}cm" stroke="#000000" strokewidth="0.03125cm"></line>
		<line x1="{pos[0]}cm" y1="{maxd + 1}cm" x2="{pos[0] + width}cm" y2="{maxd + 1}cm" stroke="#000000" strokewidth="0.0625cm"></line>
		'''.strip().replace('\n', '').replace('\t', '')
	if ppos:
		ts += f'<line x1="{ppos[0]}cm" y1="{ppos[1]}cm" x2="{pos[0] + width / 2}cm" y2="{pos[1] + .5}cm" stroke="#0000ff" strokewidth="0.0625cm"></line>' # move to fg / topmost layer?
	return ts


def csvg(tree: tuple[tuple | None], leafs: tuple[tuple[float, int]]):
	y = (max(leaf[1] for leaf in leafs) + 1) * 2
	x = len(leafs)
	ts = rcsvg(tree, width = x, maxd = max(leaf[1] for leaf in leafs))
	svg = f'''
	<svg width="{x}cm" height="{y}cm" version="1.1" xmlns="http://www.w3.org/2000/svg">
		<g id="graph">
			{ts}
		</g>
		<use href="#graph" y="{y / 2}cm" transform="rotate(180, {x / 2}, {y / 2})"></use>
	</svg>
	'''.strip().replace('\n', '').replace('\t', '') # BUG: transform doesn't work yet

	with open('./output.svg', 'w') as f:
		f.write(svg)


if __name__ == '__main__':
	main()
