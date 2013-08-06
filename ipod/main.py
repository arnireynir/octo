import stagger
import os
import shutil


ALLOWED_EXTENSIONS = ['mp3','m4a']

def ipodImport(target, source):
    #Get every directory and files into list.
    lst = os.walk(target)
    for (path,dirs, files) in lst:
        for f in files:
            if f:
                pth = os.path.join(path,f)

                #Checks if soundfile is valid.
                if f[-3:] in ALLOWED_EXTENSIONS:
                    try:
                        tag = stagger.read_tag(pth)
                    except:
                        print("No tag to read: " + pth)


                    dest = os.path.join(source, tag.artist)
                    #Get the format of the file.
                    extension = os.path.splitext(f)[1]

                    if tag.album:
                        dest = os.path.join(dest,tag.album)
                        createFolder(dest)
                        shutil.copy2(pth, dest)

                        if tag.title:
                            renameFile(os.path.join(dest,f), dest, tag.title, extension, tag)
                        else:
                            renameFile(os.path.join(dest,f), dest, "Unknown",  extension, tag)
                    else:
                        createFolder(dest)
                        shutil.copy2(pth, dest)

                        if tag.title:
                            renameFile(os.path.join(dest,f), dest, tag.title, extension, tag)
                        else:
                            renameFile(os.path.join(dest,f), dest, "Unknown",  extension, tag)


#Renames file if title present else prints error to console.
def renameFile(source, dest, name, extension,tag):
    try:
        if tag.track:
            name = str(tag.track) + ' - ' + str(tag.title)
        os.rename(source, os.path.join(dest,name) + extension)
    except:
        print("Failed rename: " + source)

#Creates folder if not already exist.
def createFolder(name):
    if not os.path.exists(name):
        os.makedirs(name)


ipodImport('ipod', 'source')

