import os
import shutil
import time
def main():
    deletedfolder=0
    deletedfiles=0
    path="/pathtodelete"
    days=30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        for rootfolder,folders,files in os.walk(path):
            if seconds>=getfileorfolder(rootfolder):
                removefolder(rootfolder)
                deletedfolders+=1
                break
            else:
                for folder in folders:
                    folderpath=os.path.join(rootfolder,folder)
                    if seconds>=getfileorfolder(folderpath):
                        removefolder(folderpath)
                        deletedfolders+=1
                for file in files:
                    filepath=os.path.join(rootfolder,file)
                    if seconds>=getfileorfolder(filepath):
                        removefile(filepath)
                        deletedfiles+=1
    else:
        if seconds>=getfileorfolder(path):
                removefile(path)
                deletedfiles+=1
        else:
            print("path not found")
            deletedfiles+=1
    print("folders deleted",deletedfolder)
    print("filesdeleted",deletedfiles)
def removefolder(path):
    if not shutil.rmtree(path):
        print("path removed successfully")
    else:
        print("unable to delete path")
def removefile(path):
    if not os.remove(path):
        print("path removed successfully")
    else:
        print("unable to delete path")
def getfileorfolder(path):
    seetime=os.stat(path).st_ctime
    return seetime
if __name__=='__main__':
    main()