#!/usr/bin/env python
import services.common.tools as tools # Custom module for shared functions
import services.common.lists as lists
import json # Allows conversion to and from json

# Specifies kind of data to retrieve from PhosPhAt
API_METHOD = 'getHotspotData'

# search function is required by Adama
def search(args):
    """Uses PhosPhAt API to return phosphorylation hotspots when given
    an AGI code.

    Args:
        All arguments are stored in a single dict.
        transcript_id: AGI Transcript Identifier. Refers to a specific protein.
            Example value: 'AT1G06410.1'
    """
    tools.validate_args(args)

    # Saves dict of hotspots retrieved from API call
    hotspots = tools.request_data(args['transcript_id'], API_METHOD)

    # hotspots['result'] refers to a dict within hotspots that stores the data
    for h in hotspots['result']:
        extracted_data = {}
        extracted_data['hotspot_sequence'] = h['hsp_hotspot_sequenz']
        extracted_data['start_position'] = h['hsp_hotspot_start']
        extracted_data['end_position'] = h['hsp_hotspot_stop']
        # Adama requires JSON objects be separated by three dashes
        print json.dumps(extracted_data) + '\n---'

# Returns a list of valid transcript IDs
def list(args):
    print lists.HOTSPOT
