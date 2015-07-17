import requests # Allows for HTTP requests to be made
import json # Allows conversion to and from json
import tools # Custom module allowing access to PhosPhAt API
from requests.exceptions import ConnectionError
from threading import Thread
# Specify kind of data to retrieve from PhosPhAt
API_METHOD = 'getExperimentsModAa'

# Adama API that returns a list of all transcript IDs; no parameters
PROTEIN_API_URL = ('https://api.araport.org/community/v0.3/jk-dev/'
        'protein_api_v0.1/list')

# Adama requires a token to access their API
TOKEN = '29f28472195bbd2c28ffb4c9360ab81'



f = ''

def blah(transcript):
    #try:
    phosphat_response = tools.request_data(transcript, API_METHOD)
    if phosphat_response['result']: # If result is not empty
        f.write(transcript+'\n')
    #except ConnectionError:
    #    print "EXCEPTION ON:" + transcript



def main():
    """Creates a file containing a list of transcript IDs that PhosPhAt has
        phosphorylation data for.

    Args: none

    Raises:
    """

    # Retrieve a JSON object containing a list of all possible transcripts.
    protein_api_result = requests.get(PROTEIN_API_URL, headers={'Authorization': 'Bearer ' + TOKEN })
    protein_api_result.raise_for_status()
    protein_api_result = json.loads(protein_api_result.text)

    # Extract the list of transcripts
    all_transcripts = protein_api_result['result'][0]

    thread_list = []

    f = open('valid_transcripts1.txt', 'w')
    for transcript in all_transcripts:
        thread = Thread(target = blah, args={transcript,})
        thread.start()
        thread_list.append(thread)


    for thread in thread_list:
        thread.join()

    f.close()

if __name__ == '__main__':
    main()
