import qrcode
import os,sys
import getopt

def oneQR(name,link):
    img = qrcode.make(link)
    img.save(str(name)+".png")
    print("created "+str(name)+".png")

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
        inputFile = r"test.txt"
    links = open(inputFile,'r')
    nameIncrement = 0
    try:
        os.makedirs('pictures')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
        else:
            print('pictures dir already exist')
    for link in links:
        oneQR(r'pictures\\'+str(nameIncrement),link)
        nameIncrement = nameIncrement + 1
