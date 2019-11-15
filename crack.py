import zipfile
from time import time

'''


Zip password cracker
By Dictionary password attack
Using Python


'''

def main():
    try:
        myZip = zipfile.ZipFile("CTF.zip")
    except zipfile.BadZipfile:
        print "There was an error opening your zip file."
        return

    password = ''
    
    print "Password cracking started..."
    print " "
    print "                    "
    print "                    "
    print "                         _   "
    print "      ___ _ __ __ _  ___| | ____      ____ _ _ __ ___   "
    print "     / __| '__/ _` |/ __| |/ /\ \ /\ / / _` | '__/ _ \  "
    print "    | (__| | | (_| | (__|   <  \ V  V / (_| | | |  __/  "
    print "     \___|_|  \__,_|\___|_|\_\  \_/\_/ \__,_|_|  \___|  "
    print "                                                " 
    print "                        Malware                             "
    print "                        mAlware                             "
    print "                        maLware                             "
    print "                        malWare                             "
    print "                        malwAre                             "
    print "                        malwaRe                             "  
    print "                        malwarE                             "
    print "                  "
    print "              "
    print " "
    print "Please wait...."
    timeStart = time()
    with open("rockyou.txt", "r") as f:
        passes = f.readlines()
        for pass_count, x in enumerate(passes):
            password = x.strip()
            try:
                myZip.extractall(pwd = password)
                totalTime = time() - timeStart
                print "\nPassword cracking successful: %s\n" % password
                print "%i Password tried per second " % (pass_count/totalTime)
                print " "
                print "For thanking us, subscribe our channel defalt th"
                print "join us malware"
                return
            except Exception as e:
                if str(e[0]) == 'Bad password for file':
                    pass # TODO: properly handle exceptions?
                elif 'Error -3 while decompressing' in str(e[0]):
                    pass # TODO: properly handle exceptions?
                else:
                    print e
        print "Please try another passwords list file"
        print "For more cracker script, subscribe our channel"
        print "defalt th"

if __name__ == '__main__':
	main()
