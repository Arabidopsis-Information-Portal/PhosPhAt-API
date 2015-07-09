#!/usr/bin/env python
import services.common.tools as tools
import json

# Specify kind of data to retrieve from PhosPhAt
API_METHOD = 'getPredictedAa'

def search(args):
    """Uses PhosPhAt API to get predicted phosphorylation sites.

    Args:
        All arguments are stored in a single dict.
        transcript_id: AGI Transcript Identifier. Refers to a specific protein.
            Example value: 'AT1G06410.1'
    """
    tools.validate_args(args)

    # Save dict of phosphorylation sites retrieved from API call
    phos_sites = tools.request_data(args['transcript_id'], API_METHOD)

    filtered_phos_sites = []
    # phos_sites['result'] refers to a dict in phos_sites that has the data
    for p in phos_sites['result']:
        extracted_data = {}
        extracted_data['position_in_protein'] = p['prd_position']
        extracted_data['prediction_score'] = p['prd_score']
        extracted_data['13mer_sequence'] = p['prd_13mer']
        print json.dumps(extracted_data) + '\n---'

def list(args):
    raise Exception('Not implemented yet')
