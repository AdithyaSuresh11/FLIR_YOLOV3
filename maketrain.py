



import os


txtlist = os.listdir("/media/ray/Files/FILRdataset/FLIR_ADAS/training/PreviewData/")

for a in txtlist:
    print("/media/ray/Files/FILRdataset/FLIR_ADAS/training/PreviewData/"+a, file=open("/home/ray/Documents/darknet/darknet/FLIR/flir_train.txt","a"))

print("jobs done!")


