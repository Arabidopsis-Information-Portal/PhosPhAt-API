#!/usr/bin/env python
import services.common.tools as tools
import json

# Specify kind of data to retrieve from PhosPhAt
API_METHOD = 'getExperimentsModAa'

def search(args):
    """Uses PhosPhAt API to return a summary of experimental
    phosphorylation sites.

    Args:
        All arguments are stored in a single dict.
        transcript: AGI transcript identifer. Refers to a specific protein.
            Example value: 'AT1G06410.1'
    """
    tools.validate_args(args)
    # Save dict of phosphorylation sites retrieved from API call
    phos_sites = tools.request_data(args['transcript'], API_METHOD)

    phos_summary = {}
    # phos_sites['result'] refers to a dict in phos_sites that has the data
    for p_site in phos_sites['result']:
        # Save modified sequences and peptide ids
        phos_summary[p_site['pep_id']] = p_site['modifiedsequence']

    # Convert dict to a JSON object, then print it.
    # The tools.print_data() function is not used because
    # that funtion accepts a list of dicts, and this is simply one.
    print json.dumps(phos_summary) + '\n---'

def list(args):
    raise Exception('Not implemented yet')
