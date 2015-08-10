# A Python module that allows for HTTP requests to be made.
import requests
# A Python module that allows conversion to and from json.
import json
# A Python module that allows for the use of regular expressions
import re

# Original API url on which all parameters are added. This base URL is used to
# create a complete URL.
# A complete url with all parameters added looks like the following:
# http://phosphat.uni-hohenheim.de/PhosPhAtHost30/productive/views/PreJsonMeth.php?method=getExperimentsModAa&protid="AT1G01540.1"
# In this case the API method is 'getExperimentsModAa' and the transcript ID is 'AT1G01540.1'.
# A complete URL is used to contact the remote host PhosPhAt via HTTP requests.
API_BASE_URL = ('http://phosphat.uni-hohenheim.de/PhosPhAtHost30'
        '/productive/views/PreJsonMeth.php')

def request_data(transcript_id, api_method):
    """Returns data from an API call to PhosPhAt.

    Args:
        transcript_id: AGI Transcript Identifier.
        api_method: Specific method to call on the API.

    Returns:
        A dict deserialized from a JSON object.
    """
    # payload is a dict of arguments to be added to the url
    payload = {}
    # The API requires transcript_id to be surrounded by quotes.
    payload['protid'] = '"' + transcript_id + '"'
    payload['method'] = api_method

    # Combine base url with parameters and return data
    response = requests.get(API_BASE_URL, params=payload)
    # Verify that a response was actually received.
    response.raise_for_status()
    return json.loads(response.text)

def validate_args(args):
    """Validates a transcript_id given a dict of arguments.

    Args:
        args: A dict containing the arguments to verify.

    Raises:
        TypeError: If 'transcript_id' is not found in 'args'.
        ValueError: If 'transcript_id' is given but invalid.
    """
    # Verify if transcript_id was given
    if not ('transcript_id' in args):
        raise TypeError('Missing required argument (transcript_id)')

    transcript_id = args['transcript_id'].strip()

    # Verify the transcript_id is valid by checking its format via
    # a regular expression.
    p = re.compile('^AT[1-5CM]G[0-9]{5,5}\.[0-9]{1,3}$', re.IGNORECASE)
    if not p.search(transcript_id):
        raise ValueError('Not a valid transcript_id')

def expand_mod_type(short_version):
    """Exapnds the modification type to a human readable description.

    Args:
        short_version: a modification type code from PhosPhAt.

    Returns:
        The equivalent human readable version of the modification code.
        If there was no equivalent found, it returns the original code.
    """
    switcher = {
        'phos' : 'experimental/validated phosphorylation site',
        'phos_amb' : 'ambiguous phosphorylation site',
        'ox' : 'site of oxidized methionine',
        'ox_amb': 'ambiguous site of oxidized methionine'
    }
    # Used switcher.get('key') over switcher['key'] to prevent a KeyError.
    # The second parameter is the value returned in case the key can't be found.
    return switcher.get(short_version, short_version)
