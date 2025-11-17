with open('./inp/silben08.txt', 'r') as f:
	txt = f.read()
	f.close()


def getitem(list: list, i: int):
	try:
		return list[i]
	except IndexError:
		return ''


con = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ß']
voc = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'ü']
zwi = ['ai', 'au', 'ei', 'eu', 'oi', 'ui', 'äu']

# Lars' rules
gen = ''
for w in txt.strip().split(' '):
	punctuation = ''.join([c for c in w if c in ['.', ',', '?', '!']])  # only punctuation marks used in the examples
	w = w.strip('.,?!')
	wgen = ''
	w = [c for c in w]
	for i in range(len(w)):
		im2 = getitem(w, i - 2)
		im1 = getitem(w, i - 1)
		i0 = getitem(w, i)
		i1 = getitem(w, i + 1)
		i2 = getitem(w, i + 2)
		# no split after last c
		if i == len(w) - 1:
			wgen += i0
			continue
		# rule 4
		if i0 in voc and not (i1 in con and i2 in con):
			wgen += i0 + '-'
			continue
		elif i0 in voc:
			wgen += i0
			continue
		# rule 3
		if i0 in con and i1 in con and i2 in con: # split after first con
			wgen += i0 + '-'
			continue
		if im1 in con and i0 in con and i1 in con: # no split after second con
			wgen += i0
			continue
		# rule 2
		if i == 0 or i == len(w) - 2:
			wgen += i0
			continue
		# rule 1
		if i0 in con and i1 in con:
			wgen += i0 + '-'
			continue
		wgen += i0 # if no rule added a split
	gen += wgen + punctuation + ' '
			
gen = gen.strip()

print(gen)
