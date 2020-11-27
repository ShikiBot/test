from django.shortcuts import render
import requests
from xml.etree import ElementTree

IDs = ["R01010", "R01020A", "R01035", "R01060", "R01090B", "R01100", "R01115", "R01135", "R01200", "R01200"]


response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
tree = ElementTree.fromstring(response.content).find('Valute[@ID="R01235"]')
Value = tree.find('Value').text
Name = tree.find('Name').text

# Create your views here.
def index(request):
    return render(
        request,
        'index.html',
        context={
            'name': Name,
            'value': Value
            },
    )