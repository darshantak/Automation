from unsplash_search import UnsplashSearch
import subprocess
import urllib.request as ur
import ctypes,random
from threading import Timer


def changer(path,filename,key):

    genres=["mountains","dog","river","graffiti","buildings","roads","night","instrument","stars","moon"]
    wall=random.choice(genres)
    unsplash=UnsplashSearch(key)
    img=unsplash.search_photo(wall)

    fullpath=path+filename
    fullpath
    url=img['img']
    url
    ur.urlretrieve(url+".jpg",fullpath)

    # downloaded=fullpath[1:-1]
    # downloaded
    ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:\\workspace_python\\Projects\\downloads\\newimage.jpg" , 0)
# subprocess.run('REG ADD "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d D:\\workspace_python\\Projects\\downloads\\newimage.jpg  /f',shell=True)
# subprocess.run("RUNDLL32.EXE user32.dll, UpdatePerUserSystemParameters",shell=True)

    Timer(10,changer).start()


#set path where you want to download images
path=r'D:\\workspace_python\\Projects\\downloads\\'
filename='newimage.jpg'
#access key
key="AlrColMRzUm_LFqRVAIijhwUC6khPqqSLMNGjSiG5ek"
changer(path,filename,key)