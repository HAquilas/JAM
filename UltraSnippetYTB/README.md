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
This program utilizes the YouTube Data API to search for and retrieve information about music videos. To use this program, you need to provide your own YouTube Data API key.

Once you have obtained your YouTube Data API key, you can configure it in an environment variable on your machine. Here is how to do it:

    On Linux/MacOS:

export YOUTUBE_API_KEY="YOUR_API_KEY"

    On Windows:

set YOUTUBE_API_KEY=YOUR_API_KEY

Example

python3  Youtube.py -v 100000 -c US -j 30