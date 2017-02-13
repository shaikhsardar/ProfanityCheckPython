import urllib

def read_text():
    quotes = open("C:\Users\yoyosar\OOP Python\movies_quote.txt")
    content_of_file = quotes.read()
    print(content_of_file)
    quotes.close()
    check_profanity(content_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=+text_to_check")
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!")
    elif "false" in output:
        print("This document has no curse Words!")
    else:
        print("Could not scan the document properly.")
read_text()
