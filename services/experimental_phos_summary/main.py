#!/usr/bin/env python
import re
import services.common.tools as tools


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

    phos_summary = []

    for p_site in phos_sites['result']:
        # Save modified sequences and peptide ids
        current_phos = {}
        current_phos['modified_sequence'] = p_site['modifiedsequence']
        current_phos['modified_sequence_id'] = p_site['pep_id']
        phos_summary.append(current_phos)

    # Remove duplicates in list by changing values from: dict->tuple->set->dict
    phos_summary = [dict(t) for t in set(
                            [tuple(d.items()) for d in phos_summary])]
    
    tools.print_data(phos_summary)


def list(args):
    raise Exception('Not implemented yet')
