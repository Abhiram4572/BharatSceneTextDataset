import sys
import os
import json
from tqdm import tqdm

# read BSTD.json
with open(os.path.join(os.getcwd(), "BSTD.json")) as f:
    data = json.load(f)

# get all languages
languages = []
for key, value in data.items():
    language = value["language"]
    if language not in languages:
        languages.append(language)


# create a data folder
dataFolder = os.path.join(os.getcwd(), "data")
if not os.path.exists(dataFolder):
    os.makedirs(dataFolder)

# create a folder for each language inside data folder
for language in languages:
    languageFolder = os.path.join(dataFolder, language)
    if not os.path.exists(languageFolder):
        os.makedirs(languageFolder)
    

def downloadImg(image_url, image_name, language):

    path_to_save = os.path.join(dataFolder, language, image_name)
    if os.path.exists(path_to_save):
        print(f'{path_to_save} already exists')
        return
    
    try:
        # download the image using wget 
        os.system(f'wget {image_url} -O {path_to_save}')
    except:
        print(f'Error in downloading {image_url}')

    return


allUrls = [value['url'] for key, value in data.items()]
allImageNames = [value['image_name'].split("/")[-1] for key, value in data.items()]
allLanguages = [value['language'] for key, value in data.items()]

for i in tqdm(range(len(allUrls))):
    downloadImg(allUrls[i], allImageNames[i], allLanguages[i])