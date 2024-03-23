# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# # Clé d'API YouTube Data
# api_key = 'AIzaSyAY2_AqCmF8jEr3K5WoZHI9UXmjoaoclU8'  # Remplacez par votre propre clé d'API YouTube Data

# # Seuil de vues
# views_min = 500000000  # Définissez le seuil de vues souhaité
# views_max = 1000000000
# # Création de l'objet YouTube Data API
# youtube = build('youtube', 'v3', developerKey=api_key)

# try:
#     # Recherche de vidéos musicales
#     search_response = youtube.search().list(
#         q='music',
#         type='video',
#         part='snippet',
#         maxResults=50  # Nombre maximal de résultats à récupérer
#     ).execute()

#     # Récupération des titres de musique avec un nombre de vues supérieur au seuil
#     music_titles = []
#     for item in search_response['items']:
#         video_id = item['id']['videoId']
#         video_response = youtube.videos().list(
#             id=video_id,
#             part='snippet,statistics'
#         ).execute()
#         view_count = int(video_response['items'][0]['statistics']['viewCount'])
#         if view_count > views_min and view_count < views_max:
#             title = item['snippet']['title']
#             music_titles.append(title)

#     # Affichage des titres de musique
#     for title in music_titles:
#         print(title)
#     if len(music_titles) == 0:
#         print("NOT FOUND !")

# except HttpError as e:
#     print('Une erreur HTTP est survenue : ', e)

# 2EME  ----------------------------------------------------------------------


# import argparse
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# from datetime import datetime, timedelta

# # Clé d'API YouTube Data
# api_key = 'AIzaSyAY2_AqCmF8jEr3K5WoZHI9UXmjoaoclU8'  # Remplacez par votre propre clé d'API YouTube Data

# # Création de l'objet YouTube Data API
# youtube = build('youtube', 'v3', developerKey=api_key)

# # Analyse des arguments de ligne de commande
# parser = argparse.ArgumentParser(description='Recherche de vidéos musicales sur YouTube.')
# parser.add_argument('-v', '--views', type=int, required=True, help='Nombre de vues minimales')
# parser.add_argument('-c', '--country', type=str, required=True, help='Code du pays')
# parser.add_argument('-j', '--age', type=int, required=True, help='Nombre de jours depuis la sortie')
# args = parser.parse_args()

# # Paramètres de recherche
# views_threshold = args.views  # Nombre de vues minimales
# country_code = args.country  # Code du pays (ex: 'FR' pour la France)
# max_age = timedelta(days=args.age)  # Âge maximal de la vidéo

# try:
#     # Recherche de vidéos musicales du pays spécifié
#     search_response = youtube.search().list(
#         q='music',
#         type='video',
#         part='snippet',
#         maxResults=50,  # Nombre maximal de résultats à récupérer
#         regionCode=country_code  # Filtre par pays
#     ).execute()

#     # Récupération des titres de musique avec un nombre de vues supérieur au seuil et âge adéquat
#     music_titles = []
#     for item in search_response['items']:
#         video_id = item['id']['videoId']
#         video_response = youtube.videos().list(
#             id=video_id,
#             part='snippet,statistics'
#         ).execute()
#         view_count = int(video_response['items'][0]['statistics']['viewCount'])
#         published_at = video_response['items'][0]['snippet']['publishedAt']
#         published_date = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')
#         video_age = datetime.utcnow() - published_date
#         if view_count > views_threshold and video_age > max_age:
#             title = item['snippet']['title']
#             music_titles.append(title)

#     # Affichage des titres de musique
#     for title in music_titles:
#         print(title)
#     if len(music_titles) == 0:
#         print("NOT FOUND !")

# except HttpError as e:
#     print('Une erreur HTTP est survenue : ', e)

#  3EME -------------------------------------------------------------------
import argparse
import random
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime, timedelta
import os

# Clé d'API YouTube Data
api_key = os.environ.get('YOUTUBE_API_KEY')
if not api_key:
    raise ValueError('Clé d\'API YouTube Data non définie dans les variables d\'environnement.')  # Remplacez par votre propre clé d'API YouTube Data

# Création de l'objet YouTube Data API
youtube = build('youtube', 'v3', developerKey=api_key)

# Analyse des arguments de ligne de commande
parser = argparse.ArgumentParser(description='Recherche de vidéos musicales sur YouTube.')
parser.add_argument('-v', '--views', type=int, default=random.randint(100000, 1000000),
                    help='Nombre de vues minimales (défaut : valeur aléatoire entre 100 000 et 1 000 000)')
parser.add_argument('-c', '--country', type=str, default='US',
                    help='Code du pays (défaut : US)')
parser.add_argument('-j', '--age', type=int, default=5000,
                    help='Nombre de jours depuis la sortie (défaut : valeur aléatoire entre 1 et 30)')
args = parser.parse_args()

# Paramètres de recherche
views_threshold = args.views  # Nombre de vues minimales
country_code = args.country  # Code du pays
max_age = timedelta(days=args.age)  # Âge maximal de la vidéo

try:
    # Vérification de la validité du code du pays
    region_response = youtube.i18nRegions().list(part='snippet').execute()
    valid_country_codes = [item['snippet']['gl'] for item in region_response['items']]
    if country_code not in valid_country_codes:
        raise ValueError('Code de pays invalide.')

    # Recherche de vidéos musicales du pays spécifié
    search_response = youtube.search().list(
        q='music',
        type='video',
        part='snippet',
        maxResults=50,  # Nombre maximal de résultats à récupérer
        regionCode=country_code  # Filtre par pays
    ).execute()

    # Récupération des titres de musique avec un nombre de vues supérieur au seuil et âge adéquat
    
    # Avant  -------------------------------------------------------------------------
    # music_titles = []
    # for item in search_response['items']:
    #     video_id = item['id']['videoId']
    #     video_response = youtube.videos().list(
    #         id=video_id,
    #         part='snippet,statistics'
    #     ).execute()
    #     view_count = int(video_response['items'][0]['statistics']['viewCount'])
    #     published_at = video_response['items'][0]['snippet']['publishedAt']
    #     published_date = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')
    #     video_age = datetime.utcnow() - published_date
    #     if view_count > views_threshold and video_age < max_age:
    #         title = item['snippet']['title']
    #         music_titles.append(title)
    # Avant   ------------------------------------------------------------------------
    
    music_videos = []
    for item in search_response['items']:
        video_id = item['id']['videoId']
        video_response = youtube.videos().list(
            id=video_id,
            part='snippet,statistics'
        ).execute()
        view_count = int(video_response['items'][0]['statistics']['viewCount'])
        published_at = video_response['items'][0]['snippet']['publishedAt']
        published_date = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')
        video_age = datetime.utcnow() - published_date
        if view_count > views_threshold and video_age < max_age:
            title = item['snippet']['title']
            video_link = f"https://www.youtube.com/watch?v={video_id}"
            music_videos.append((title, video_link))
    
    # Affichage des titres de musique
    
    #  Avant  -----------------------------------------
    
    # for title in music_titles:
    #     print(title)
    # if len(music_titles) == 0:
    #      print("NOT FOUND !")
    
    #  Avant  --------------------------------------------
    
    for title, video_link in music_videos:
        print(f"Titre : {title}")
        print(f"Lien : {video_link}\n")

except ValueError as e:
    print('Erreur :', e)

except HttpError as e:
    print('Une erreur HTTP est survenue :', e)

# 4EME -------------------------------------------------------------------

# import argparse
# import random
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# from datetime import datetime, timedelta

# # Clé d'API YouTube Data
# api_key = 'AIzaSyAY2_AqCmF8jEr3K5WoZHI9UXmjoaoclU8'  # Remplacez par votre propre clé d'API YouTube Data

# # Création de l'objet YouTube Data API
# youtube = build('youtube', 'v3', developerKey=api_key)

# # Analyse des arguments de ligne de commande
# parser = argparse.ArgumentParser(description='Recherche de vidéos musicales sur YouTube.')
# parser.add_argument('-v', '--views', type=int, default=random.randint(100000, 1000000),
#                     help='Nombre de vues minimales (défaut : valeur aléatoire entre 100 000 et 1 000 000)')
# parser.add_argument('-c', '--country', type=str, default='US',
#                     help='Code du pays (défaut : US)')
# parser.add_argument('-j', '--age', type=int, default=random.randint(1, 30),
#                     help='Nombre de jours maximum depuis la sortie (défaut : valeur aléatoire entre 1 et 30)')
# args = parser.parse_args()

# # Paramètres de recherche
# views_threshold = args.views  # Nombre de vues minimales
# country_code = args.country  # Code du pays
# max_age = timedelta(days=args.age)  # Âge maximal de la vidéo
# min_age = timedelta(days=args.age - 1)  # Âge minimal de la vidéo (jours précédents)

# try:
#     # Vérification de la validité du code du pays
#     region_response = youtube.i18nRegions().list(part='snippet').execute()
#     valid_country_codes = [item['snippet']['gl'] for item in region_response['items']]
#     if country_code not in valid_country_codes:
#         raise ValueError('Code de pays invalide.')

#     # Recherche de vidéos musicales du pays spécifié
#     search_response = youtube.search().list(
#         q='music',
#         type='video',
#         part='snippet',
#         maxResults=50,  # Nombre maximal de résultats à récupérer
#         regionCode=country_code  # Filtre par pays
#     ).execute()

#     # Récupération des titres de musique avec un nombre de vues supérieur au seuil et âge adéquat
#     music_titles = []
#     for item in search_response['items']:
#         video_id = item['id']['videoId']
#         video_response = youtube.videos().list(
#             id=video_id,
#             part='snippet,statistics'
#         ).execute()
#         view_count = int(video_response['items'][0]['statistics']['viewCount'])
#         published_at = video_response['items'][0]['snippet']['publishedAt']
#         published_date = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')
#         video_age = datetime.utcnow() - published_date
#         if view_count > views_threshold and min_age <= video_age <= max_age:
#             title = item['snippet']['title']
#             music_titles.append(title)

#     # Affichage des titres de musique
#     for title in music_titles:
#         print(title)
#     if len(music_titles) == 0:
#          print("NOT FOUND !")

# except ValueError as e:
#     print('Erreur :', e)

# except HttpError as e:
#     print('Une erreur HTTP est survenue :', e)