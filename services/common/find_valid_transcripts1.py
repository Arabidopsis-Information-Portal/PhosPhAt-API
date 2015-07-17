import requests # Allows for HTTP requests to be made
import json # Allows conversion to and from json
import tools # Custom module allowing access to PhosPhAt API
from requests.exceptions import ConnectionError
from threading import Thread
import threading
import thread
# Specify kind of data to retrieve from PhosPhAt
API_METHOD = 'getExperimentsModAa'

# Adama API that returns a list of all transcript IDs; no parameters
PROTEIN_API_URL = ('https://api.araport.org/community/v0.3/jk-dev/'
        'protein_api_v0.1/list')

# Adama requires a token to access their API
TOKEN = 'b844c42e6de0e476f8eea4a06baa212b'

lock = threading.Lock()

def blah(transcript, f):
    try:
        phosphat_response = tools.request_data(transcript, API_METHOD)
        if phosphat_response['result']: # If result is not empty
            f.write(transcript+'\n')
    except Exception as e:
        lock.acquire()
        print e.__str__() + "\n ----"
        lock.release()
        #thread.interrupt_main()
        #print "EXCEPTION ON:" + transcript



def main():
    """Creates a file containing a list of transcript IDs that PhosPhAt has
        phosphorylation data for.

    Args: none

    Raises:
    """

    # Retrieve a JSON object containing a list of all possible transcripts.
    protein_api_result = open('protein_list.txt','r').read()
    protein_api_result = json.loads(protein_api_result)

    # Extract the list of transcripts
    all_transcripts = protein_api_result['result'][0]

    thread_list = []

    f = open('valid_transcripts1.txt', 'w')
    for transcript in all_transcripts:
        thread1 = Thread(target = blah, args=[transcript, f])
        thread1.start()
        thread_list.append(thread1)


    for thread1 in thread_list:
        thread1.join()
        print 'done'
    f.close()

if __name__ == '__main__':
    main()
