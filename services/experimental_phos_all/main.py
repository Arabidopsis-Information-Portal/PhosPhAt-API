#!/usr/bin/env python
import re
import services.common.tools as tools


API_METHOD = 'getExperimentsModAa'
# Uses PhosPhAt API to return all experimental phosphorylation sites.


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
        # Save all relevant data
        current_phos = {}
        current_phos['peptide_sequence'] = p_site['pep_sequence']
        current_phos['position_in_protein'] = p_site['position']
        current_phos['modification_type'] = tools.expand_mod_type(
                p_site['modificationType'])
        current_phos['modified_sequence_id'] = p_site['pep_id']
        phos_summary.append(current_phos)

    tools.print_data(phos_summary)


def list(args):
    raise Exception('Not implemented yet')
