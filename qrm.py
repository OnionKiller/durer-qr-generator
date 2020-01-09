import qrcode
import os,sys
import getopt

#added magic, merege done succesfully

def oneQR(name,link):
    img = qrcode.make(link)
    img.save(str(name)+".png")
    print("created "+str(name)+".png")

def method_name():
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
    return inputFile

if __name__ == "__main__":
    inputFile = method_name()
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
        makeOneQR(r'pictures\\'+str(nameIncrement),link)
        nameIncrement = nameIncrement + 1
