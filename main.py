def combinantorial(lst):
    count = 0
    index = 1
    pairs = []
    for element1 in lst:
        for element2 in lst[index:]:
            pairs.append((element1, element2))
        index += 1
    return pairs

def findOptimalTransition(pairs):
	maximum_interest      = -1
	maximum_interest_pair = ()
	for pair in pairs:
		new_interest = pair[0].interestFactor(pair[1])
		if (new_interest > maximum_interest_pair):
			maximum_interest      = new_interest
			maximum_interest_pair = (pair[0], pair[1])
	return maximum_interest_pair, maximum_interest


