import urllib as url
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except url.error.URLError:
    print(f'O site Pudim não está acessível no momento.')
else:
    print(f'Consegui acessar o site Pudim com sucesso!')
    print(site.read())
