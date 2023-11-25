from google_images_search import GoogleImagesSearch
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY_CSE')
cx = os.getenv('CX')

gis = GoogleImagesSearch(api_key, cx)

search_params = {
    'q': 'Fred Chicken', # Your Specific Search
    'num': 10,  # the number you want to download
    'safe': 'high', # image quality
}

gis.search(search_params=search_params)

for image in gis.results():
    image.download('image')
