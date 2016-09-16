import urllib
def read_text():
    quotes=open("C:\Python27\Doc\script.txt")
    contens_of_file = quotes.read()
    print( contens_of_file )
    quotes.close()
    check_profanity(contens_of_file)
    
def check_profanity( text ):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text)
    output = connection.read()
    connection.close()
    if "true" in output:
        print(" Profanity Alter")
    elif "false" in output:
        print ("This document has no curse words")
    else:
        print("Could not scan the document")
read_text()
