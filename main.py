#!/usr/bin/env python
import search_types
import urllib
import requests
import json
import re

URL = ('http://phosphat.uni-hohenheim.de/PhosPhAtHost30'
        '/productive/views/PreJsonMeth.php')

# Uses PhosPhAt API to return experimental or predicted phosphorylation sites
# or phosphorylation hotspots when given an AGI code.

def search(args):
    # args contains a dict with a minimum of two key:values
    # dict keys with example values:
    # 'transcript':'AT1G06410.1'
    #       --> (required) AGI transcript identifer.
    #           Refers to a specific protein.
    # 'search_type':'experimental'
    #       --> (required) the type of search to be performed. options are:
    #           'experimental','predicted','hotspot'
    # 'modified_sequence':'SY(pT)NLLDLASGNFPVMGR'
    #       --> (optional) a modified peptide sequence. should only be given if
    #           performing an 'experimental' search. if it is not given and
    #           search_type = 'exprimental', a list of sequences is returned
    #

    if not ('transcript' in args and 'search_type' in args):
        raise TypeError('Missing required arguments')

    transcript = args['transcript'].strip()

    p = re.compile('^AT[1-5CM]G[0-9]{5,5}\.[0-9]{1,3}$', re.IGNORECASE)
    if not p.search(transcript):
        raise ValueError('Not a valid transcript')


    # PhosPhAt API requires transcript to be surrounded by '%22'
    payload = {}
    payload['protid'] = urllib.unquote('%22' + transcript + '%22')

    # Perform specific search type
    if args['search_type'] == 'experimental':
        # GET data from PhosPhAt
        payload['method'] = 'getExperimentsModAa'
        r = requests.get(URL, params=payload)
        phos_sites = json.loads(r.text)
        mod_seq = args.get('modified_sequence')

        search_types.print_experimental(phos_sites, mod_seq)

    elif args['search_type'] == 'predicted':
        payload['method'] = 'getPredictedAa'
        r = requests.get(URL, params=payload)
        phos_sites = json.loads(r.text)

        search_types.print_predicted(phos_sites)

    elif args['search_type'] == 'hotspot':
        payload['method'] = 'getHotspotData'
        r = requests.get(URL, params=payload)
        phos_sites = json.loads(r.text)

        search_types.print_hotspot(phos_sites)

def list(args):
    raise Exception('Not implemented yet')
