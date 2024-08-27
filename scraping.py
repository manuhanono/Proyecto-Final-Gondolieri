key = "AIzaSyAcsPgpQQIZ3i-BKm4tVvwTiK_B-oyqA8Q"
buscador = "738b24c8b43fe4c05"
#"https://cse.google.com/cse.js?cx=738b24c8b43fe4c05" es el buscador propio

import pandas as pd

df = pd.read_excel("Ofertas Perfumeria Agosto.xlsx")

from google_images_search import GoogleImagesSearch
gis = GoogleImagesSearch(key, buscador)

products = df["DESCRIPCIÓN"]
paths = []
for product in products:
    _search_params = {
        'q': product,
        'num': 1,
        'searchType': 'image',
        'imgType': 'photo',
        'imgSize': 'medium',
        'safe': 'off',
        'fileType': 'jpg|gif|png'
    }

    # this will search and download:
    gis.search(search_params=_search_params, path_to_dir='/Users/manu/Proyecto Final/Proyecto-Final-Gondolieri/imagenes_productos_scrapeo'
               ,  custom_image_name=product)
    paths.append(f"imagenes_productos_scrapeo/{product}.jpg")

