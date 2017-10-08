


####################################

########## Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'cbefffc9aa6d473693e3fac7e7fd47dd',
}

body = '{"url":"http://a.abcnews.com/images/Politics/GTY_obama_cf_151230_1_16x9_992.jpg"}'
params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()

except Exception as e:
    print(e.message())
