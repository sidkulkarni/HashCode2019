def inBoth(slide_1, slide_2):
	intersection = slide_1.tags.intersection(slide_2.tags)
	return len(intersection), intersection

def inOneNotTwo(slide_1, slide_2):
	difference   = slide_1.tags.difference(slide_2.tags)
	return len(difference), difference

def inTwoNotOne(slide_1, slide_2):
	difference   = slide_2.tags.difference(slide_1.tags)
	return len(difference), difference

def interestFactor(slide_1, slide_2):
	score1, _ =  inBoth(slide_1, slide_2)
	score2, _ =  inOneNotTwo(slide_1, slide_2)
	score3, _ =  inTwoNotOne(slide_1, slide_2)
	return min(score1, score2, score3)
