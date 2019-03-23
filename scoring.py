def scoreSlideArray(slidesArray):
	score = 0
	for i in range(len(slidesArray) - 1):
		slide_1 = slidesArray[i]
		slide_2 = slidesArray[i + 1]
		score = score + slide_1.interestFactor(slide_2)
	return score
