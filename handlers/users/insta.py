import requests
def insta_save(link):
    url = "https://instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com/get-info-rapidapi"

    querystring = {"url":link}

    headers = {
        "x-rapidapi-key": "4360836b63msh9edf45be1d447e0p105946jsn831c2c920c00",
        "x-rapidapi-host": "instagram-downloader-download-instagram-videos-stories1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    rasmlar = []
    try:
        for i in response.json()["medias"]:
            try:
                rasmlar.append(i["download_url"])
            except KeyError:
                pass
        return {"images": rasmlar}
    except KeyError:
        try:
            return {"video": response.json()["download_url"]}
        except KeyError:
            return {"error": "Hech qanday media topilmadi"}