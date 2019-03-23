class Photo:
    def __init__(self, orient, tags, ID):
        self.orient = orient    #the string H or V to indicate the orientation
        self.tags = tags #array of tags (strings)
        self.ID = ID    #the id number of the photo

class Slide:
    def __init__(self, photos):
        self.photos = photos
        self.tags   = 0

    def computeTags(self):
        if (len(self.photos) == 1):
            self.tags = self.photos[0].tags
        else:
            tags_0    = self.photos[0].tags
            tags_1    = self.photos[1].tags
            self.tags = tags_0.union(tags_1)    
