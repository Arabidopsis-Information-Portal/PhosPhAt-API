#!/usr/bin/env python
import services.common.tools as tools


API_METHOD = 'getExperimentsModAa'

def search(args):
    """Uses PhosPhAt API to return all experimental phosphorylation sites.

    Args:
        All arguments are stored in a single dict.
        transcript: AGI transcript identifer. Refers to a specific protein.
            Example value: 'AT1G06410.1'
    """
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
        phos_summary.append(current_phos)

    tools.print_data(phos_summary)


def list(args):
    raise Exception('Not implemented yet')
