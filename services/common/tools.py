import urllib
import requests
import json
import re

API_BASE_URL = ('http://phosphat.uni-hohenheim.de/PhosPhAtHost30'
        '/productive/views/PreJsonMeth.php')


def request_data(transcript, api_method):
    payload = {}
    # TODO: Find a neater way to encapsulate transcript in '%22'
    payload['protid'] = urllib.unquote('%22' + transcript + '%22')
    payload['method'] = api_method

    response = requests.get(API_BASE_URL, params=payload)
    return json.loads(response.text)

def print_data(data):
    if data is not None:
        for d in data:
            print json.dumps(d) + '\n---'

def validate_args(args, mod_seq=False):

    # Validate transcript
    if not ('transcript' in args):
        raise TypeError('Missing required argument (transcript)')

    transcript = args['transcript'].strip()
    p = re.compile('^AT[1-5CM]G[0-9]{5,5}\.[0-9]{1,3}$', re.IGNORECASE)

    if not p.search(transcript):
        raise ValueError('Not a valid transcript')
    if mod_seq:
        if ('modified_sequence_id' not in args):
            raise TypeError('Missing required argument (modified_sequence_id)')



def expand_mod_type(short_version):
    switcher = {
        'phos' : 'experimental/validated phosphorylation site',
        'phos_amb' : 'ambiguous phosphorylation site',
        'ox' : 'site of oxidized methionine'
    }
    return switcher.get(short_version, short_version)
