class Anime:
   def __init__(self, name, genres):
    self.name = name
    self.genres = genres 
    
#FullMetal_Alchemist = Anime("FullMetalAlchemist",["School","Romance","Drama","Fantasy","Magic","Military","Shouren"])
#KimiNoNawa = Anime("KimiNoNaWa",["Drama","Romance","School","Supernatural"])


def match(Anime1,Anime2):
    match_coefficient = 0
    genres1 = Anime1.genres
    genres2 = Anime2.genres
    for genre1 in genres1:
        for genre2 in genres2:
            if (genre1 == genre2):
                print(f"Matched genres: {genre1}")
                match_coefficient += 1
    if (match_coefficient >= ((min(len(genres1),len(genres2)))/2)):
        print("It's a match")
    else :
        print("It's not a match")
  
#match(FullMetal_Alchemist,KimiNoNawa)

