#!/usr/bin/env python
import services.common.tools as tools

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
    hotspots = tools.request_data(args['transcript'], API_METHOD)

    for h in hotspots['result']:
        extracted_data = {}
        extracted_data['hotspot_sequence'] = h['hsp_hotspot_sequenz']
        extracted_data['start_position'] = h['hsp_hotspot_start']
        extracted_data['end_position'] = h['hsp_hotspot_stop']

        filtered_hotspots.append(extracted_data)

    tools.print_data(filtered_hotspots)

def list(args):
    raise Exception('Not implemented yet')
