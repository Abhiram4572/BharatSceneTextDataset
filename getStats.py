import json
import os
import sys

language = sys.argv[1]

finalDataFolder = os.path.join(os.getcwd(), "files")

if language != "punjabi":
    languageFile = os.path.join(finalDataFolder, language + '.json')
    
    with open(languageFile) as f:
        data = json.load(f)

else:
    languageFile1 = os.path.join(finalDataFolder, 'punjabi_part1.json')
    languageFile2 = os.path.join(finalDataFolder, 'punjabi_part2.json')

    with open(languageFile1) as f:
        data1 = json.load(f)
    
    with open(languageFile2) as f:
        data2 = json.load(f)
    
    data = {**data1, **data2}

print(f'No of images: {len(data)}')
wordCounts = []
for key, value in data.items():
    wordCounts.append(len(value['coordinates']))

print(f'Avg no of words per image: {sum(wordCounts)/len(wordCounts)}')