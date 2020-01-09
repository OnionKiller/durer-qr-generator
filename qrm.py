import qrcode
import os,sys
import getopt

def oneQR(name,link):
    img = qrcode.make()
    img.save(name+".png")
    print("created "+name+".png")

if __name__ == "__main__":
    inputFile = ''
    try:
        opts,args = getopt.getopt(sys.argv[1:],"hi:",["iFile"])
    except getopt.GetoptError:
        print ("qrm.py -i <input file>")
        sys.exit(2)
    for opt,arg in args:
        if opt == "-h":
            print("qrm.py -i <input file>")
            sys.exit()
        elif opt in ("-i","--iFile"):
            inputFile = arg
    if inputFile == '':
        inputFile = r"D:\Dürer\infoMCS\qrMaker\qrMaker\test.txt"
    links = open(inputFile,'r')
    nameIncrement = 0
    for link in links:
        oneQR(nameIncrement,link)