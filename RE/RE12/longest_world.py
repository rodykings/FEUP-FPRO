import requests

def longest_word(url):
    
    import urllib.request
    response = urllib.request.urlopen('https://en.wikipedia.org/wiki/Monty_Python')
    html = response.read().decode()
    
    print(html)
#    return html
print(longest_word("hey"))