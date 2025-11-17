def main():
	with open('./inp/drehfreudig16.txt', 'r') as f:
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


def rcsvg(tree: tuple[tuple | None], width: float = 1, depth: int = 0, maxd: int = 0, pos: tuple[float, float] = (0, 0), ppos: tuple[float, float] | None = None) -> tuple[str, str]:
	if tree:
		ls = f'''
		<line x1="{pos[0]}" y1="{pos[1]}" x2="{pos[0] + width}" y2="{pos[1]}" stroke="#000000" stroke-width="0.03125"></line>
		<line x1="{pos[0]}" y1="{pos[1]}" x2="{pos[0]}" y2="{pos[1] + 1}" stroke="#000000" stroke-width="0.03125"></line>
		<line x1="{pos[0] + width}" y1="{pos[1]}" x2="{pos[0] + width}" y2="{pos[1] + 1}" stroke="#000000" stroke-width="0.03125"></line>
		'''.strip().replace('\n', '').replace('\t', '')
		cs = f'''
		<circle cx="{pos[0] + width / 2}" cy="{pos[1] + .5}" r="0.0625" fill="#ff0000"></circle>
		'''.strip().replace('\n', '').replace('\t', '')
		xo = 0
		for node in tree:
			gen = rcsvg(node, width = width / len(tree), depth = depth + 1, maxd = maxd, pos = (pos[0] + xo, pos[1] + 1), ppos = (pos[0] + width / 2, pos[1] + .5))
			ls += gen[0]
			cs += gen[1]
			xo += width / len(tree)
	else:
		ls = f'''
		<line x1="{pos[0]}" y1="{pos[1]}" x2="{pos[0] + width}" y2="{pos[1]}" stroke="#000000" stroke-width="0.03125"></line>
		<line x1="{pos[0]}" y1="{pos[1]}" x2="{pos[0]}" y2="{maxd + 1}" stroke="#000000" stroke-width="0.03125"></line>
		<line x1="{pos[0] + width}" y1="{pos[1]}" x2="{pos[0] + width}" y2="{maxd + 1}" stroke="#000000" stroke-width="0.03125"></line>
		<line x1="{pos[0]}" y1="{maxd + 1}" x2="{pos[0] + width}" y2="{maxd + 1}" stroke="#000000" stroke-width="0.0625"></line>
		'''.strip().replace('\n', '').replace('\t', '')
		cs = f'''
		<circle cx="{pos[0] + width / 2}" cy="{pos[1] + .5}" r="0.0625" fill="#ff0000"></circle>
		'''.strip().replace('\n', '').replace('\t', '')
	if ppos:
		ls += f'<line x1="{ppos[0]}" y1="{ppos[1]}" x2="{pos[0] + width / 2}" y2="{pos[1] + .5}" stroke="#0000ff" stroke-width="0.0625"></line>' # move to fg / topmost layer?
	return ls, cs


def csvg(tree: tuple[tuple | None], leafs: tuple[tuple[float, int]]):
	y = (max(leaf[1] for leaf in leafs) + 1) * 2
	x = len(leafs)
	gen = '\n'.join(rcsvg(tree, width = x, maxd = max(leaf[1] for leaf in leafs)))
	svg = f'''
	<svg width="{x}cm" height="{y}cm" viewBox="0, 0, {x}, {y}" version="1.1" xmlns="http://www.w3.org/2000/svg">
		<g id="graph">
			{gen}
		</g>
		<use href="#graph" y="{y / 2}" transform=" translate(0, {y / 2}) rotate(180, {x / 2}, {y / 2})"></use>
	</svg>
	'''.strip().replace('\n', '').replace('\t', '') # BUG: transform doesn't work yet

	with open('./output.svg', 'w') as f:
		f.write(svg)


if __name__ == '__main__':
	main()
