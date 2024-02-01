# Bharat Scene Text Dataset

[comment]: <> (Add a table with 13 languages and links to its files)

# Release updates:

[comment]: <> (checkbox style release updates with cross ticks for the ones present)

- [30/9/24] Data v1 released for 12 languages along with the detection annotations.

### UpNext
- [ ] Recognition annotation release.
- [ ] Data v1 release for Marathi.
- [x] Detection annotations for 12 languages.
- [x] Data v1 for 12 languages.

# Data Description:
## Data Statistics:

| Language | #images | #Avg words per image |
| :---: | :---: | :---: |
| Assamese | 295 | 27.1 |
| Bengali | 305 | 32 | 
| Gujarati | 525 | 9.1 |
| Hindi | 1218 | 14.7 | 
| Kannada | 627 | 14.2 | 
| Malayalam | 474 | 14.5 | 
| Odia | 533 | 20 |
| Punjabi | 517 | 38.7 |
| Tamil | 521 | 10.4 | 
| Telugu | 607 | 10.5 |
| Urdu | 551 | 21.4 | 
| Meitei | 82 | 19.9 |
 Marathi | 100 | 1.5 |


## Data Download:

Step 1: Download the zip file from [here](https://drive.google.com/file/d/1Ct7-PHyBguyvY6A0zvmz4s_JOoav21pE/view?usp=share_link)

Step 2: Extract the downloaded zip file into "data" folder
```
unzip BSTD.zip -d data
```
Step 3: Download the images
```
python3 downloadImages.py 
```

## Data Format:
Words in the image are annotated in the polygon format. The annotation file is a json file with the following format:
```
"language_image_id": {
    "annotations": 
    {
        "polygon_0":
        {
            "coordinates":
                [
                    [x1, y1],
                    [x2, y2],
                    ...,
                    [xn, yn]
                ],
            "text": "text in the current polygon"
        },
        ...,
        "polygon_n":
        {
            "coordinates":
                [
                    [x1, y1],
                    [x2, y2],
                    ...,
                    [xn, yn]
                ],
            "text": "text in the current polygon"
        }
    },
    "url": "url of the image",
    "image_name": "name of the image",
    "language": "main language"
}
```

## Data Visualisation:
To visualise detection annotations, run the following command:
```
python3 visualise.py <image_path> <path_to_BSTD.json>
```
for e.g.
```
python3 visualise.py data/assamese/image_1005.jpg data/BSTD.json
```

Some examples are below:
<!-- Add an example image next to this line -->
![image info](visualised_images/image.jpg)
![image info](visualised_images/image2.jpg)

## Known Issues:
- The data is collected from the internet and hence there are some images which are not in the correct orientation. We have tried to remove such images but there might be some left. 

## Data Annotation
- All the images are collected from Wikimedia commons (under Creative Commons Licence, cc-by-sa-4.0)
- Further detection and recognition annotations are human annotated.

# Contact
For any queries, please contact us at:
- [Anand Mishra](mailto:mishra@iitj.ac.in)
- [Abhirama Subramanyam](mailto:penamakuri.1@iitj.ac.in)
