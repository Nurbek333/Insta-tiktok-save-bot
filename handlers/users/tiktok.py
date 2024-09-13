import requests

def tiktok_save(link):
    url = f"https://tikwm.com/api/?url={link}"
    response = requests.get(url)
    
    data = response.json().get('data', {})
    
    video = data.get('play')
    images = data.get('images')
    music = data.get('music')
    
    return {
        'video': video,
        'images': images,
        'music': music
    }