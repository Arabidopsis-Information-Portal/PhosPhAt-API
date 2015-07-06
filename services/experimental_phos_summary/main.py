#!/usr/bin/env python
import services.common.tools as tools
import json


API_METHOD = 'getExperimentsModAa'
# Uses PhosPhAt API to return a summary of experimental phosphorylation sites.


def search(args):
    # args contains a dict a single key:value pair
    # dict key with example value:
    # 'transcript':'AT1G06410.1'
    #       --> (required) AGI transcript identifer.
    #           Refers to a specific protein.

    tools.validate_args(args)

    phos_sites = tools.request_data(args['transcript'], API_METHOD)

    phos_summary = {}

    for p_site in phos_sites['result']:
        # Save modified sequences and peptide ids
        phos_summary[p_site['pep_id']] = p_site['modifiedsequence']

    print json.dumps(phos_summary) + '\n---'

def list(args):
    raise Exception('Not implemented yet')
