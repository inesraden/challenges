import random
songnames=["a","b","c","d","e","f","g","h","i","j"]
artistnames=[]
arr=[]

for a in range(10):
  arr.append(songnames)

for i in range (len(arr)):
  print(arr[i])

lastsong=0
lastlastsong=0
for x in range(100):
  artist=0
  while artist==lastsong or artist==lastlastsong:
    artist=random.randint(0,10)
  currentchoice=(artist,random.choice(songnames))
  print(currentchoice)
  lastlastsong=lastsong
  lastsong=artist



