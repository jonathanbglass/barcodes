import os
from os import listdir
from os.path import isfile, join
import argparse
import requests
import shutil
import time

# 861094493354-cfvvblgc9a0ukdk3ouomj3pdb599qeml.apps.googleusercontent.com
# ue4c3mBtH8srX9p6xV2ujkck
def gen_large(upc):
    url = "http://www.waspbarcode.com/barcode-maker"
    print (upc)
    payload = {'q':'python',
        '__VIEWSTATE':'/wEPDwUKMTUwMzg1NjgzMg8WAh4TVmFsaWRhdGVSZXF1ZXN0TW9kZQIBFgICBxBkZBYCAgMPZBYCZg9kFgJmD2QWCAIJDxYEHgRUZXh0BSJQbGVhc2UgZW50ZXIgYSB2YWxpZCBlbWFpbCBhZGRyZXNzHgdWaXNpYmxlZ2QCCw8PFgIeCEltYWdlVXJsBUd+L3NlcnZpY2VzL3dhc3BiYXJjb2RlL2JhcmNvZGVnZW4uYXNoeD9zeW1ib2xvZ3k9VXBjQSZjb2RlPTg3NDY5MDAwOTk3N2RkAg0PFgIeC18hSXRlbUNvdW50AgIWBAIBD2QWAmYPFQQGYWN0aXZlATABMA1CYXJjb2RlIE1ha2VyZAICD2QWAmYPFQQAATEBMRFCYXJjb2RlIEVkdWNhdGlvbmQCDw8WAh8EAgIWBAIBD2QWAmYPFQIHIGFjdGl2ZQEwZAICD2QWAmYPFQIAATFkZHjHXvL5sBFh3oL22n2YQK7tNVuNUFf8ckcshJRfT4xo',
        '__VIEWSTATEGENERATOR': 'D2163E31',
        '__EVENTVALIDATION': '/wEdABBZEZXJCrXVLa4/ZCCdg+ptp6Wh9EdvDOtAY7Kw6QJZBahOTAnKTVDqtmKphJo8TEXQnYXUIRSWjp6YpdzbGcVy1H7Lp7UqDhmRJQXvvUQVESrSvRBeaiRDN+dziPPpbMQe8fGpYxpBDyOINs6Js4HnPaWuJlNQyjbNvwNvvXiHYpBv0ry8hoG5zy58yO8NR4hwYULD/xQDE5+DRqDqsB9UrxCQcRSIL0HndruRNlianUlI7p5F0NYPySEUDybhMD6uLaXkb+BrSP5DHdWZcwmLiRmX6xsjdlvskrKlxB7M8eQuCE6VNfx2Sqr3tnHNfjPh4uoE4MrSwShG8jl8PJ5VAJGoDkNcRQZ826H3634uP8/MzH4Z3yZDTwgFhWz6Png=',
        'ph_content_0$ddlType': 'UPC-A',
        'ph_content_0$txtCode': upc,
        'ph_content_0$txtEmail': 'jonathan.glass@gmail.com',
        'ph_content_0$ctl00': 'Generate'  }
    r = requests.post(url, payload)
    return

def gen_thumbnail(upc):
    thumbnailurl="http://www.waspbarcode.com/services/waspbarcode/barcodegen.ashx?symbology=UpcA&amp;code="+upc
    t = requests.get(thumbnailurl, stream=True)
    if t.status_code == 200:
        with open("attachments/"+upc+".png", 'wb') as out_image:
            shutil.copyfileobj(t.raw, out_image)
        del t
    else:
        print (t.status_code, t.headers['content-type'], t.encoding)
    return

def check_files(upc):
    if os.path.exists('labels/'+upc+'_thumbnail.png'):
        print ('labels/'+upc+'_thumbnail.png exists')
    else:
        print ("gen_thumbnail("+upc+")")
        gen_thumbnail(upc)
    if os.path.exists('labels/'+upc+'_large.png'):
        print ('labels/'+upc+'_large.png exists')
    else:
        print ("gen_large("+upc+")")
        gen_large(upc)
    return

def main():
    translation_table = dict.fromkeys(map(ord, '*\n'), None)
    url = "http://www.waspbarcode.com/barcode-maker"
    a = open('c:/output/upcs','r')
    for line in a:
        upc = line.translate(translation_table)
        check_files(upc)

if __name__ == "__main__":
    main()
