import urllib.request

def longest_word(url):
    
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    url_words = set(html.split())
    
    response1 = urllib.request.urlopen("https://raw.githubusercontent.com/fpro-admin/recitas/master/words")
    html1 = response1.read().decode()
    url1_words = set(html1.split())
    
    intersect = url_words.intersection(url1_words)
    
    return sorted(intersect, key=lambda x:len(x), reverse=True)[0]
    
