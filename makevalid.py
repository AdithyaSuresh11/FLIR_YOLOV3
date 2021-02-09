



import os


txtlist = os.listdir("/media/ray/Files/FILRdataset/FLIR_ADAS/validation/PreviewData/")

for a in txtlist:
    print("/media/ray/Files/FILRdataset/FLIR_ADAS/validation/PreviewData/"+a, file=open("/home/ray/Documents/darknet/darknet/FLIR/flir_valid.txt","a"))

print("jobs done!")


