import stagger
import os
import shutil


ALLOWED_EXTENSIONS = ['mp3','m4a']

def ipodImport(target, source):
    lst = os.walk(target)

    for (path,dirs, files) in lst:

        for f in files:
            if f:
                pth = os.path.join(path,f)
                if f[-3:] in ALLOWED_EXTENSIONS:
                    try:
                        tag = stagger.read_tag(pth)
                    except:
                        print("No tag to read: " + pth)


                    dest = os.path.join(source, tag.artist)
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



def renameFile(source, dest, name, extension,tag):
    try:
        os.rename(source, os.path.join(dest,name) + extension)
    except:
        print("Failed rename: " + source)

def createFolder(name):
    if not os.path.exists(name):
        os.makedirs(name)


ipodImport('ipod', 'source')

#list(t)
#tag.artist
#tag.album
#tag.title




#tag = stagger.read_tag('ipod/F00/JDSA.mp3')
#list(t)
#tag.artist
#tag.album
#tag.title