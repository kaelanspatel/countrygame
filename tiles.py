import random

# This code by D. Knuth
def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
      if random.randrange(num): continue
      line = aline
    return line

terrain_types = ["ap", "ds", "gl", "rf", "tu", "ar", "mt", "wl"]
# ap -> ARID PLAINS
# ds -> DESERT
# gl -> GRASSLANDS
# rf -> RAINFOREST
# tf -> TEMPERATE FOREST
# tu -> TUNDRA
# ar -> ARCTIC
# mt -> MOUNTAINS
# wl -> WASTELAND

class Tile:
    
    def __init__(self, name = None, terrain = None):
        
        if not name:
            with open("words.txt") as word_file:
                self.name = random_line(word_file).strip().capitalize() + random.choice([" Sound", " Ford", " Acres",  " Glen", "land", "wood", "shire", " Point"])
        else:
            self.name = name    
        
        
        if not terrain:
            self.terrain = random.choice(terrain_types)
        else:
            self.terrain = terrain
            
    def __str__(self):    
        
        if self.terrain == "ap":
            terrain_string = "Arid Plains"
        elif self.terrain == "ds":
            terrain_string = "Desert"
        elif self.terrain == "gl":
            terrain_string = "Grasslands"
        elif self.terrain == "rf":
            terrain_string = "Rainforest"
        elif self.terrain == "tf":
            terrain_string = "Temperate Forest"
        elif self.terrain == "tu":
            terrain_string = "Tundra"
        elif self.terrain == "ar":
            terrain_string = "Arctic"
        elif self.terrain == "mt":
            terrain_string = "Mountains"
        elif self.terrain == "wl":
            terrain_string = "Wasteland"
      
        
        return self.name + ": " + terrain_string