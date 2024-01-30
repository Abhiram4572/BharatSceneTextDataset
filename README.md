# Bharat Bhasha in Scenes

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

| Language | #images | #Avg words per image | Annotation File |
| :---: | :---: | :---: | :---: |
| Assamese | 295 | 27.1 | [file](files/assamese.json) |
| Bengali | 305 | 32 | [file](files/bengali.json) |
| Gujarati | 525 | 9.1 | [file](files/gujarati.json) |
| Hindi | 1218 | 14.7 | [file](files/hindi.json) |
| Kannada | 627 | 14.2 | [file](files/kannada.json) |
| Malayalam | 474 | 14.5 | [file](files/malayalam.json) |
| Odia | 533 | 20 | [file](files/odia.json) |
| Punjabi | 517 | 38.7 | [part1](files/punjabi_part1.json), [part2](files/punjabi_part2.json) |
| Tamil | 521 | 10.4 | [file](files/tamil.json) |
| Telugu | 607 | 10.5 | [file](files/telugu.json) |
| Urdu | 551 | 21.4 | [file](files/urdu.json) |
| Marathi | 100 | 1.5 | [file]() |


All these statistics can be verified by quickly running the following command:

```bash
python3 getStats.py <language_in_lower_case>
```

for e.g.
```bash
python3 getStats.py hindi
```

## Data Format:
Words in the image are annotated in the polygon format. The annotation file is a json file with the following format:
```
"image_id": {
    "coordinates": 
    {
        "coordinates":
            [
                [x1, y1],
                [x2, y2],
                ...,
                [xn, yn]
            ],
        "text": "text in the image"
    },
    "url": "url of the image",
    "image_name": "name of the image",
}
```

## Known Issues:
- The data is collected from the internet and hence there are some images which are not in the correct orientation. We have tried to remove such images but there might be some left. 

# Contact
For any queries, please contact us at:
- [Anand Mishra](mailto:mishra@iitj.ac.in)
- [Abhirama Subramanyam](mailto:penamakuri.1@iitj.ac.in)
