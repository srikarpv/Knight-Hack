from __future__ import print_function
import time
import requests
import cv2
import operator
import numpy as np
import subprocess
import re
from decimal import Decimal
import io
import requests

response = requests.get('http://my-ulr.com')
print response.status_code

# Import library to display results
import matplotlib.pyplot as plt
# Display images within Jupyter
# plt.plot(range(10))
# plt.show()

list_of_samples = []
final_res = {}
final_res["neutral"] = []
final_res["sadness"] = []
final_res["happiness"] = []
final_res["disgust"] = []
final_res["anger"] = []
final_res["surprise"] = []
final_res["fear"] = []
final_res["contempt"] = []

_url = 'https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize'
f = open('./localconfigkeys')

_key = f.readline().splitlines()[0]
f.close() #Here you have to paste your primary key
_maxNumRetries = 10

# Returns file length in milliseconds
def getLength(filename):
    result = subprocess.Popen(["ffprobe", filename], stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    info =  [x for x in result.stdout.readlines() if "Duration" in x]
    duration = info[0].split(",")[0]
    parsed_duration = re.split('[^0-9]', duration)
    parsed_duration.reverse()
    time = parsed_duration[:3]
    parsed_time =  list(map((lambda x: int(x)), time))
    return parsed_time[0] + parsed_time[1] * 1000 + parsed_time[2] * 1000 * 60


def processRequest( json, data, headers, params ):

    """
    Helper function to process the request

    Parameters:
    json: Used when processing images from its URL. See API Documentation
    data: Used when processing image read from disk. See API Documentation
    headers: Used to pass the key information and the data type request
    """

    retries = 0
    result = None

    while True:

        response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )

        if response.status_code == 429:

            print( "Message: %s" % ( response.json()['error']['message'] ) )

            if retries <= _maxNumRetries:
                time.sleep(1)
                retries += 1
                continue
            else:
                print( 'Error: failed after retrying!' )
                break

        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0:
                result = None
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str):
                if 'application/json' in response.headers['content-type'].lower():
                    result = response.json() if response.content else None
                elif 'image' in response.headers['content-type'].lower():
                    result = response.content
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json()['error']['message'] ) )

        break

    return result

def renderResultOnImage( result, img ):

    '''Display the obtained results onto the input image'''

    for currFace in result:
        faceRectangle = currFace['faceRectangle']
        l = len(currFace['scores'])
        d = {}

        print (currFace['scores'])
        for key, value in currFace['scores'].iteritems():
            #print ("The key is ", key, "and the value is ", value)
            d[key] = value
        list_of_samples.append(d)
        for k,v in d.iteritems():
            print (k, v)
        currEmotion = max(currFace['scores'].items(), key=operator.itemgetter(1))[0]

        textToWrite = "%s" % ( currEmotion )
        #cv2.putText( img, textToWrite, (faceRectangle['left'],faceRectangle['top']-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 1 )

def create_final_res(f_res):
    final_res = {}
    final_res["neutral"] = []
    final_res["sadness"] = []
    final_res["happiness"] = []
    final_res["disgust"] = []
    final_res["anger"] = []
    final_res["surprise"] = []
    final_res["fear"] = []
    final_res["contempt"] = []
    for sample in f_res:

        for feature, value in sample.iteritems():

            feature_array = final_res[feature]
            feature_array.append(value)
            final_res[feature] = feature_array
    return final_res

# Load raw image file into memory
# pathToFileInDisk = r'./Images/trump.jpg'
# with open( pathToFileInDisk, 'rb' ) as f:
#     data = f.read()
def execute():
    vidcap = cv2.VideoCapture('./Images/Filename.mp4')
    vid_len = (getLength('Filename.mp4'))


    for i in range(0, vid_len/3000):
        vidcap.set(cv2.CAP_PROP_POS_MSEC, i*3000)      # just cue to 20 sec. position
        success,image = vidcap.read()
        if success:
            cv2.imwrite("frame.jpg", image)     # save frame as JPEG file
            pathToFileInDisk = r'./frame.jpg'
            with open( pathToFileInDisk, 'rb' ) as f:
                data = f.read()
        #cv2.imshow("20sec",image)
        #cv2.waitKey()

            headers = dict()
            headers['Ocp-Apim-Subscription-Key'] = _key
            headers['Content-Type'] = 'application/octet-stream'

            json = None
            params = None

            result = processRequest( json, data, headers, params )

            if result is not None:
            # Load the original image from disk

                data8uint = np.fromstring( data, np.uint8 ) # Convert string to an unsigned int array
                img = cv2.cvtColor( cv2.imdecode( data8uint, cv2.IMREAD_COLOR ), cv2.COLOR_BGR2RGB )

                renderResultOnImage( result, img )

    ig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow( img, aspect = 'auto')
    plt.show()
execute()
fin_res = create_final_res(list_of_samples)

for f in fin_res.iteritems():
    print (f)
def write_to_datapoints_file(datapoints):

    fname = "datapoints.txt"
    target = open(fname, 'w')
    for feature,value in datapoints.iteritems():
        target.write(feature)
        target.write('\n')
        for elem in value:
            target.write(str(elem))
            target.write('\n')

    target.close()

write_to_datapoints_file(fin_res)
