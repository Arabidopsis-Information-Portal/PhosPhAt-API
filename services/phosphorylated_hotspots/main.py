#!/usr/bin/env python
import services.common.tools as tools
import json
# Specifies kind of data to retrieve from PhosPhAt
API_METHOD = 'getHotspotData'

def search(args):
    """Uses PhosPhAt API to return phosphorylation hotspots when given
    an AGI code.

    Args:
        All arguments are stored in a single dict.
        transcript: AGI transcript identifer. Refers to a specific protein.
            Example value: 'AT1G06410.1'
    """
    tools.validate_args(args)

    filtered_hotspots = []
    # Saves dict of hotspots retrieved from API call
    hotspots = tools.request_data(args['transcript'], API_METHOD)

    # hotspots['result'] refers to a dict within hotspots that stores the data
    for h in hotspots['result']:
        extracted_data = {}
        extracted_data['hotspot_sequence'] = h['hsp_hotspot_sequenz']
        extracted_data['start_position'] = h['hsp_hotspot_start']
        extracted_data['end_position'] = h['hsp_hotspot_stop']
        print json.dumps(extracted_data) + '\n---'


def list(args):
    raise Exception('Not implemented yet')
