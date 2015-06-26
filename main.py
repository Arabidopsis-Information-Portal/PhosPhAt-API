#!/usr/bin/env python
import search_types
import urllib
import requests
import json

URL = 'http://phosphat.uni-hohenheim.de/PhosPhAtHost30/productive/views/PreJsonMeth.php'

# Uses PhosPhAt API to return experimental or predicted phosphorylation sites
# or phosphorylation hotspots when given an AGI code.

def search(args):
    # args contains a dict with a minimum of two key:values
    # dict keys with example values:
    # 'locus':'At1G06410.1'
    #       --> (required) locus is an AGI code
    # 'search_type':'experimental'
    #       --> (required) the type of search to be performed. options are:
    #           'experimental','predicted','hotspot'
    # 'modified_sequence':'SY(pT)NLLDLASGNFPVMGR'
    #       --> (optional) a modified peptide sequence. should only be given if performing
    #           an 'experimental' search. if it is not given and
    #           search_type = 'exprimental', then a list of sequences is returned

    if not ('locus' in args and 'search_type' in args):
        return

    # PhosPhAt API requires locus to be surrounded by '%22'
    payload = {}
    payload['protid'] = urllib.unquote('%22' + args['locus'].upper().strip() + '%22')

    # Perform specific search type
    if args['search_type'] == 'experimental':
        # GET data from PhosPhAt
        payload['method'] = 'getExperimentsModAa'
        r = requests.get(URL, params=payload)
        phos_sites = json.loads(r.text)
        
        search_types.experimental(phos_sites, args.get('modified_sequence'))

    elif args['search_type'] == 'predicted':
        payload['method'] = 'getPredictedAa'
        r = requests.get(URL, params=payload)
        phos_sites = json.loads(r.text)

        search_types.predicted(phos_sites)

    elif args['search_type'] == 'hotspot':
        payload['method'] = 'getHotspotData'
        r = requests.get(URL, params=payload)
        phos_sites = json.loads(r.text)

        search_types.hotspot(phos_sites)
