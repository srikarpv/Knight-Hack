import httplib, urllib, base64

# Return a JSON of timestamped 
def getEmotionsJSON(url):

    params = urllib.urlencode(url)
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '2d3b154ad73d4d7283c62809d2ae8fbc'
    }
    try:
        connection = httplib.HTTPSCONNECTION('westus.api.cognitive.microsoft.com')
        connection.request("POST", "/emotion/v1.0/recognizable?%s" % params, "{body}", headers)
        response = connection.getresponse()
        data = response.read()
        connection.close()
        return data
    except:
        return 0
        
