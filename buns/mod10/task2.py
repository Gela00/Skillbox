import re
import requests

def get_h3_headings(url):
    response = requests.get(url)
    html = response.text
    pattern = r'<h3.*?>(.*?)</h3>'
    headings = re.findall(pattern, html)
    return headings

url = 'http://www.columbia.edu/~fdc/sample.html'
text = get_h3_headings(url)
print(text)