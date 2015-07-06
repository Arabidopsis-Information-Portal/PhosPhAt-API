#!/usr/bin/env python
import services.common.tools as tools

API_METHOD = 'getExperimentsModAa'

def _extract_data(p_site):
    """Used by 'search()' function to copy data from a given dict.

    Args:
        p_site: The current dict the 'search()' function is looking at

    Returns:
        A dict that contains a copy of certain values in 'p_site'.
    """
    extracted_data = {}
    extracted_data['peptide_sequence'] = p_site['pep_sequence']
    extracted_data['position_in_protein'] = p_site['position']
    extracted_data['modification_type'] = tools.expand_mod_type(
            p_site['modificationType'])
    return extracted_data

def search(args):
    """Uses PhosPhAt API to return detailed experimental phosphorylation sites
        given a modified peptide sequence.

    Args:
        All arguments are stored in a single dict.
        transcript: AGI transcript identifer. Refers to a specific protein.
            Example value: 'AT1G06410.1'
        modified_sequence: Optional. Narrows results to those matching sequence.
            Example value: '(s)(y)(t)NLLDLA(s)GNFPV(oxM)GR'
    """
    tools.validate_args(args)
    phos_sites = tools.request_data(args['transcript'], API_METHOD)

    phos_details = []
    if ('modified_sequence' not in args):
        # Saves data to a list of dicts
        for p_site in phos_sites['result']:
            current_phos = _extract_data(p_site)
            current_phos['modified_sequence'] = p_site['modifiedsequence']
            phos_details.append(current_phos)
    else:
        # Saves data if given sequence matches
        for p_site in phos_sites['result']:
            if args['modified_sequence'] == p_site['modifiedsequence']:
                current_phos = _extract_data(p_site)
                phos_details.append(current_phos)

    tools.print_data(phos_details)

def list(args):
    raise Exception('Not implemented yet')
