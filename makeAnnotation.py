#####################################################################
# Convert FLIR annotations to YoloV3 format
# Chunpeng Shao
# Dec 2018
# 
# generateList()    -> get all json filenames
# convert()         -> convert one json file to yolo format .txt file
# main()            -> entry point
#####################################################################
# USAGE:
# under Annotation folder
# >$ python3 makeAnnotation.py
# >$ mv *.txt <YOUR NEW ANNOTATION FOLDER PATH> 
#####################################################################


import os
import json

def generateList():
    rlist = []
    #flist = os.listdir("/media/ray/Files/FILRdataset/FLIR_ADAS/training/Annotations/")
    flist = os.listdir("/media/ray/Files/FILRdataset/FLIR_ADAS/validation/Annotations/")
    #flist.remove("makeAnnotation.py")
    for f in flist:
        f = f[:-5]
        rlist.append(f)
    return rlist

def convert(filename_str):
    os.mknod("/home/ray/Documents/dataset/"+filename_str+".txt")

    fp = open("/media/ray/Files/FILRdataset/FLIR_ADAS/validation/Annotations/"+filename_str+".json","r")
    data = json.load(fp)
    for a in data["annotation"]:
        x = (a["bbox"][0]+a["bbox"][2]/2)/data["image"]["width"]
        y = (a["bbox"][1]+a["bbox"][3]/2)/data["image"]["height"]
        width = (a["bbox"][2]/2)/data["image"]["width"]
        height = (a["bbox"][3]/2)/data["image"]["height"]
        categ = a["category_id"]
        #detect if there's annotation :/
        print(categ, x, y, width, height, file=open("/home/ray/Documents/dataset/"+filename_str+".txt","a"))

def main():
    filename_list = generateList()
    c = 0
    for f_str in filename_list:
        convert(f_str)
        ++c

    print("Jobs done!","total files:", c)

main()
