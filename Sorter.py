import os
from winreg import *
import time
count = 0
# Try GetHub With Tareq
def getfiletype(name):
    if name.endswith((".jpg",".png",".jpeg",".jpg",".ico",".gif",".tiff",".raw",'.exif')):
        return "Pictures"
    if name.endswith(".exe"):
        return "Programs"
    if name.endswith((".pdf",".doc",".docx","xml",'html','htm','odt','txt',"dot","dotx",'log')):
        return "Documents"
    if name.endswith((".mp3",".mp4",".vlc",'webm','mpg','mp2','mpeg','mpe','mpv','ogg','m4p','m4v','avi','wmv','mov','qt','flv','swf','avchd')):
        return "Media"
    if name == "desktop.ini":
        pass
    else:
        if name not in ["Pictures","Others","Videos","Programs","Documents"]:
            return "Others"
def getlistoffiles(patho):
    files = os.listdir(patho)
    print("[=] Found %d files. " %len(files))
    return files
def movefile(name,patho):
    os.system("move \"%s\" \"%s\"" %(name,patho))
def getdownloadsfolder():
    with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
       Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]
    return Downloads
def moveinsidedownloads(file,folder):
    global count
    movefile(getdownloadsfolder()+"\\"+file,getdownloadsfolder()+"\\"+folder)
    count += 1
def makedirs(dir):
    try:
        os.mkdir(getdownloadsfolder()+"\\"+dir)
    except:
        pass
def main():
    input("[+] Enter any key to start the sorting process (CTRL+C to cancel)")
    global count
    for file in getlistoffiles(getdownloadsfolder()):
        f_type = getfiletype(file)
        for type in ["Pictures","Programs","Documents","Media","Others"]:
            if f_type == type:
                dir = "\\%s\\" %type
                makedirs(dir)
                moveinsidedownloads(file,dir)
    print("[=] Moved %d Files!" %count)

if __name__ == "__main__":
    main()
