#UltraYoutubeMusicSnippet

## Description
It is a program that returns a list of music based on parameters such as the number of views, the number of days the video was released or the country. To set these parameters we use flags, -v for the number of views, -c for the country and -j for the number of days. This makes it easier to find sounds on Youtube Music based on these parameters.

## USAGE
To run this script, you will need Python and the following dependencies:
- google-api-python-client
-argparse

Install them using pip:
```bash
pip install google-api-python-client
pip argparse

##  Usage 
To launch the program it's just python3 followed by the name of the file with or without the flags (In mode it's optional). You can put 1 flag, 2 or all 3 at the same time.

Example

python3  Youtube.py -v 100000 -c US -j 30