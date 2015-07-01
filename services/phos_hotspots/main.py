#!/usr/bin/env python
import services.common.tools as tools


API_METHOD = 'getHotspotData'
# Uses PhosPhAt API to return phosphorylation hotspots when given an AGI code.

def search(args):
    # args contains a dict with a single key:value pair
    # dict key with example value:
    # 'transcript':'AT1G06410.1'
    #       --> (required) AGI transcript identifer.
    #           Refers to a specific protein.

    tools.validate_args(args)

    filtered_hotspots = []
    hotspots = tools.request_data(args['transcript'], API_METHOD)

    for h in hotspots['result']:
        # Rename desired keys
        h['hotspot_sequence'] = h.pop('hsp_hotspot_sequenz')
        h['start_position'] = h.pop('hsp_hotspot_start')
        h['end_position'] = h.pop('hsp_hotspot_stop')
        # Remove excess data
        h.pop('hsp_hotspot_score')
        # Add data to list
        filtered_hotspots.append(h)

    tools.print_data(filtered_hotspots)

def list(args):
    raise Exception('Not implemented yet')
