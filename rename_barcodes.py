from pyzbar.pyzbar import decode
from PIL import Image
import os
import shutil

filepath = 'attachments/'
outpath = 'labels/'
ending = '_large.png'
a = os.listdir(filepath)
for file in a:
    if "png" in file and "_thumbnail" not in file and "_large" not in file:
        bcfile=filepath+file
        print (bcfile)
        try:
            bcdecoded=decode(Image.open(bcfile))
            if bcdecoded:
                bcnum=bcdecoded[0][0].decode('UTF-8')[1:]
                newfile=outpath+bcnum+ending
                if os.path.exists(newfile):
                    print (newfile + " exists")
                    os.remove(bcfile)
                else:
                    print (newfile + 'generating')
                    shutil.copy(bcfile, newfile)
            else:
                print ('error bcdecoded = ' + bcdecoded)
        except Exception as e:
            print (str(e))
