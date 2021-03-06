from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from train_bot.models import Railway

uri = "https://api-tokyochallenge.odpt.org/api/v4/odpt:TrainInformation"
params = {"acl:consumerKey" : "ec9ea47acc38c58335396816f7fd265fb3e68f6aad1546b169005f608529a494"}
rails = Railway.objects

def index(request):
  train_bot_data = {
      'unko' : unko(),
      'railway' : rails.all()
      }
  return render(request, 'hello.html', train_bot_data)

def unko():
  unko_data = {}
  try:
    r = requests.get(uri, params = params)
  except ConnectionRefusedError:
    return unko_data
  except requests.exceptions.ConnectionError:
    return unko_data

  unko = json.loads(r.text)
  for u in unko:
    try:
      unko_data[rails.filter(railway=u['odpt:railway'])[0].title] = u['odpt:trainInformationText']
    except KeyError:
      continue
  return unko_data

