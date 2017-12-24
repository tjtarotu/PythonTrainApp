from train_bot.model import Railway
#モデル初期化用mainメソッド
if __name__=='__main__':
  import requests
  import json
  uri = "https://api-tokyochallenge.odpt.org/api/v4/odpt:Railway"
  params = {"acl:consumerKey" : "ec9ea47acc38c58335396816f7fd265fb3e68f6aad1546b169005f608529a494"}

  r = requests.get(uri, params=params)
  railways = json.loads(r.text)
  
  for railway in railways:
    title = railway['dc:title']
    rail = railway['owl:sameAs']
    operator = railway['operator']
    new_railway = Railway(title=title, railway=rail, operator=operator)
    new_railway.save()

    

