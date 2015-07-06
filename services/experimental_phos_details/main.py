#!/usr/bin/env python
import services.common.tools as tools


API_METHOD = 'getExperimentsModAa'
CHECK_MOD_SEQ = True

def search(args):
    """Uses PhosPhAt API to return detailed experimental phosphorylation sites
        given a modified peptide sequence.

    Args:
        All arguments are stored in a single dict. Both are required.
        transcript: AGI transcript identifer. Refers to a specific protein.
            Example value: 'AT1G06410.1'
        modified_sequence: Narrows results to those matching this sequence
            Example value: '(s)(y)(t)NLLDLA(s)GNFPV(oxM)GR'
    """
    tools.validate_args(args)
    if ('modified_sequence' not in args):
        raise TypeError('Missing required argument (modified_sequence)')

    phos_sites = tools.request_data(args['transcript'], API_METHOD)

    phos_details = []
    for p_site in phos_sites['result']:
        if args['modified_sequence'] == p_site['modifiedsequence']:
            # Save all relevant data
            current_phos = {}
            current_phos['peptide_sequence'] = p_site['pep_sequence']
            current_phos['position_in_protein'] = p_site['position']
            current_phos['modification_type'] = tools.expand_mod_type(
                    p_site['modificationType'])
            phos_details.append(current_phos)
    tools.print_data(phos_details)


def list(args):
    raise Exception('Not implemented yet')
