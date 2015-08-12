#!/usr/bin/env python

# services.common.tools is a custom module that contains methods shared by
# all four web services.
import services.common.tools as tools

# services.common.lists is a custom module that contains lists of valid
# transcripts that PhosPhAt has data on.
import services.common.lists as lists

# A Python module that allows conversion to and from json.
import json


# 'getHotspotData' is the method used to retrieve predicted hotspot data
# from the remote host PhosPhAt.
#
# We obtained a list of methods that could be called through personal
# communication with PhosPhAt.
API_METHOD = 'getHotspotData'

# Having a search function is required by Adama.
def search(args):
    """Uses PhosPhAt API to return computationally predicted phosphorylation
    hotspots when given an AGI code.

    Args:
        All arguments are stored in a single dict.
        transcript_id: AGI Transcript Identifier. Refers to a specific protein.
            Example value: 'AT1G06410.1'
    """
    # tools.validate_args is a custom method that validates the transcript ID.
    # It will throw an exception if the ID is invalid.
    tools.validate_args(args)

    # tools.request_data is a custom method in the services.common.tools module.
    # It contacts the remote host PhosPhAt and returns phosphorylation data
    # as a dict, which is then stored in phos_sites.
    # This method will raise an exception if it can't connect to PhosPhAt.
    hotspots = tools.request_data(args['transcript_id'], API_METHOD)

    # phos_sites is a dict, and phos_sites['result'] is a dict within phos_sites.
    for h in hotspots['result']:
        # h refers to each dict within hotspots['result'].
        extracted_data = {}
        extracted_data['hotspot_sequence'] = h['hsp_hotspot_sequenz']
        extracted_data['start_position'] = h['hsp_hotspot_start']
        extracted_data['end_position'] = h['hsp_hotspot_stop']
        # Adama requires JSON objects be printed and separated by three dashes
        print json.dumps(extracted_data) + '\n---'

# Returns a list of valid transcript IDs
def list(args):
    # Prints the list already saved in the lists module
    print json.dumps(lists.HOTSPOT)
