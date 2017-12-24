from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

uri = "https://api-tokyochallenge.odpt.org/api/v4/odpt:TrainInformation"
uri_railway =  "https://api-tokyochallenge.odpt.org/api/v4/odpt:Railway"
params = {"acl:consumerKey" : "ec9ea47acc38c58335396816f7fd265fb3e68f6aad1546b169005f608529a494"}

def index(request):
  train_bot_data = {
      'unko' : unko(),
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
  rails = railway()
  for u in unko:
    try:
      unko_data[rails[u['odpt:railway']]] = u['odpt:trainInformationText']
    except KeyError:
      continue
  return unko_data

def railway():
  railway_data = {}
  try:
    r = requests.get(uri_railway, params = params)
  except ConnectionRefusedError:
    return railway_data
  except requests.exceptions.ConnectionError:
    return railway_data

  railway = json.loads(r.text)

  for r in railway:
    try:
      railway_data[r['owl:sameAs']] = r['dc:title']
    except KeyError:
      continue

  return railway_data
