#!/usr/bin/env python
import services.common.tools as tools


API_METHOD = 'getPredictedAa'

def search(args):
    """Uses PhosPhAt API to get predicted phosphorylation sites.

    Args:
        All arguments are stored in a single dict.
        transcript: AGI transcript identifer. Refers to a specific protein.
            Example value: 'AT1G06410.1'
    """

    tools.validate_args(args)

    filtered_phos_sites = []
    phos_sites = tools.request_data(args['transcript'], API_METHOD)

    for p in phos_sites['result']:
        # Rename keys
        p['position_in_protein'] = p.pop('prd_position')
        p['prediction_score'] = p.pop('prd_score')
        p['13mer_sequence'] = p.pop('prd_13mer')
        # Remove excess data
        p.pop('prd_id')
        p.pop('prd_protein')
        p.pop('prd_type')
        # Add data to list
        filtered_phos_sites.append(p)

    tools.print_data(filtered_phos_sites)

def list(args):
    raise Exception('Not implemented yet')
