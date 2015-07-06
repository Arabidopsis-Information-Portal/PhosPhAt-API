import urllib
import requests
import json
import re

API_BASE_URL = ('http://phosphat.uni-hohenheim.de/PhosPhAtHost30'
        '/productive/views/PreJsonMeth.php')

def request_data(transcript, api_method):
    """Returns data from an API call to PhosPhAt.

    Args:
        transcript: AGI transcript identifer.
        api_method: Specific method to call on the API.

    Returns:
        A dict deserialized from a JSON object.
    """
    payload = {}
    # TODO: Find a neater way to encapsulate transcript in '%22'
    payload['protid'] = urllib.unquote('%22' + transcript + '%22')
    payload['method'] = api_method

    response = requests.get(API_BASE_URL, params=payload)
    return json.loads(response.text)

def print_data(data):
    """Prints out data as a string of JSON objects.

    Args:
        data: A list of dicts.
    """
    if data is not None:
        for d in data:
            print json.dumps(d) + '\n---'

def validate_args(args):
    """Validates a transcript given a dict of arguments.

    Args:
        args: A dict containing the arguments to verify.

    Raises:
        TypeError: If 'transcript' is not found in 'args'.
        ValueError: If 'transcript' is given but invalid.
    """
    if not ('transcript' in args):
        raise TypeError('Missing required argument (transcript)')

    transcript = args['transcript'].strip()
    p = re.compile('^AT[1-5CM]G[0-9]{5,5}\.[0-9]{1,3}$', re.IGNORECASE)

    if not p.search(transcript):
        raise ValueError('Not a valid transcript')

def expand_mod_type(short_version):
    """Swaps modification type to a human readable version.

    Args:
        short_version: a modification type code from PhosPhAt.

    Returns:
        The equivalent human readable version of the modification code.
        If there was no equivalent found, it returns the original code.
    """
    switcher = {
        'phos' : 'experimental/validated phosphorylation site',
        'phos_amb' : 'ambiguous phosphorylation site',
        'ox' : 'site of oxidized methionine'
    }
    return switcher.get(short_version, short_version)
