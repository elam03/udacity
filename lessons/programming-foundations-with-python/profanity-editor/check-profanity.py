import urllib.request

def read_text():
    f = open("movie_quotes.txt")
    contents = f.read()
    f.close()
    return contents

def check_profanity(text_to_check):
    link = 'http://www.wdylike.appspot.com'
    full_query = link + '/?q=' + text_to_check.replace(' ', '%20')
    print(full_query)
    connection = urllib.request.urlopen(full_query)
    response = connection.read()
    print(response)
    connection.close()

    # link = 'http://www.wdylike.appspot.com'
    # full_query = link + '/?q=' + text_to_check
    # connection = urllib.request.urlopen(full_query)
    # output = connection.read()
    # print(output)
    # connection.close()

data = read_text()

check_profanity(data)
# check_profanity("shotty asdf\r\n")
