#!/usr/bin/env python
import services.common.tools as tools


API_METHOD = 'getExperimentsModAa'
CHECK_MOD_SEQ_ID = True
# Uses PhosPhAt API to return detailed experimental phosphorylation sites
# given a modified peptide sequence id.

def search(args):
    # args contains a dict 2 key:value pairs
    # dict keys with example values:
    # 'transcript':'AT1G06410.1'
    #       --> (required) AGI transcript identifer.
    #           Refers to a specific protein.
    # 'modified_sequence_id':'8e32e008-0404-4b84-815b-0bac83e0f2a9'
    #       --> (required) refers to a modified peptide sequence
    #

    tools.validate_args(args, CHECK_MOD_SEQ_ID)

    phos_sites = tools.request_data(args['transcript'], API_METHOD)

    phos_details = []
    for p_site in phos_sites['result']:
        if args['modified_sequence_id'] == p_site['pep_id']:
            # Save all relevant data
            current_phos = {}
            current_phos['peptide_sequence'] = p_site['pep_sequence']
            current_phos['modified_sequence'] = p_site['modifiedsequence']
            current_phos['position_in_protein'] = p_site['position']
            current_phos['modification_type'] = tools.expand_mod_type(
                    p_site['modificationType'])
            phos_details.append(current_phos)
    tools.print_data(phos_details)


def list(args):
    raise Exception('Not implemented yet')
