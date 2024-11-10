import http.client
import json
from types import SimpleNamespace

conn = http.client.HTTPSConnection("weather-api-by-any-city.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "46d36a5e8amsh372f5d1ee38187cp10f8e5jsn3384b1b95038",
    'x-rapidapi-host': "weather-api-by-any-city.p.rapidapi.com"
}

conn.request("GET", "/weather/Bangkok", headers=headers)

res = conn.getresponse()
data = res.read()


class weather:
    def report():
        x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
        return x.current.condition.text