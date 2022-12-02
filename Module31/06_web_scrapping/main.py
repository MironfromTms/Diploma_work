import requests
import re

response = requests.get('http://www.columbia.edu/~fdc/sample.html').text
result_beta = re.findall(r'>.+</h3>', response)
release = list(map(lambda x: x[1:-5], result_beta))
print(release)

