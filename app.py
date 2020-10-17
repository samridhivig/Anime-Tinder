import csv
import random
import anime_tinder as AT 
import conversion as convert 


with open('anime.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        rows = random.sample(list(readCSV), 12295)
        random_row=random.randint(1,12292)
        anime={'name':'',
        'genre':'',
        'type':'',
        'episodes':'',
        'ratings':'',
        'members':'',
        'image':'http://placehold.it/300x200/000000/&text=Header'}

Anime1_name = input("Select Anime: ")

#removing chosen anime from the list 
genres1 = []
for row in rows:
        if row[1] == Anime1_name:
                genres1 = convert.convert(row[2])
                #rows.pop(row)
                break
print(f"Anime1 is {Anime1_name}")
Anime1 = AT.Anime(Anime1_name,genres1)

#rendering random anime profile to the user 
for row in rows: 
        name = row[1]
        genres2 = convert.convert(row[2])
        anime_type = row[3]
        episodes = row[4]
        ratings = row[5]
        members = row[6]
        print(f"Anime 2 is {name}")
        Anime2 = AT.Anime(name,genres2)
        AT.match(Anime1,Anime2)
        user_input = input('Press N for next, E for exit: ')
        if user_input == 'E' or user_input == 'e':
                break
