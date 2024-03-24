#UltraYoutubeMusicSnippet

## Description
This program is designed to generate a curated list of music videos based on specified parameters such as view count, release date, and country of origin. Users can set these parameters using flags: '-v' for view count, '-c' for country, and '-j' for the number of days since release. This streamlined approach facilitates efficient searching for music on YouTube, enabling users to refine their results according to specific criteria.

## USAGE
To run this script, you will need Python and the following dependencies:
- google-api-python-client
-argparse

Install them using pip:
```bash
pip install google-api-python-client
pip argparse

##  Usage 
To execute the program, simply use 'python3' followed by the filename, with or without the flags (in any combination). It is optional to include one flag, two flags, or all three simultaneously.

Example

python3  Youtube.py -v 100000 -c US -j 30