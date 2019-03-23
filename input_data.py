from Slide import Photo, Slide

# return a list of photos
def process_photo(filename):
    f = open(filename)
    lines = f.readlines()
    num_photo = int(lines[0].strip('\n'))
    lines = lines[1:]
    it = 0
    photos_arr = []
    for line in lines:
        line = line.strip('\n')
        items = line.split(' ')
        orient = items[0]
        tags = items[2:]
        p = Photo(orient,tags,it)
        photos_arr.append(p)
        it += 1
    f.close()
    return photos_arr

def split_photos(photos):
	horizontal_photos = []
	vertical_photos   = []
	for photo in photos:
		if photo.orient == 'H':
			horizontal_photos.append(photo)
		else:
			vertical_photos.append(photo)
	return horizontal_photos, vertical_photos

def create_slide_array(photos_arr):
