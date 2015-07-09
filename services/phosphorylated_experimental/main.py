#!/usr/bin/env python
import services.common.tools as tools
import json
# Specify kind of data to retrieve from PhosPhAt
API_METHOD = 'getExperimentsModAa'

def search(args):
    """Uses PhosPhAt API to return detailed experimental phosphorylation sites
        given a modified peptide sequence.

    Args:
        All arguments are stored in a single dict.
        transcript_id: AGI Transcript Identifier. Refers to a specific protein.
            Example value: 'AT1G06410.1'
    """
    tools.validate_args(args)
    # Save dict of phosphorylation sites retrieved from API call
    phos_sites = tools.request_data(args['transcript_id'], API_METHOD)

    phos_details = []
    # phos_sites['result'] refers to a dict in phos_sites that has the data
    for p_site in phos_sites['result']:
        extracted_data = {}
        extracted_data['peptide_sequence'] = p_site['pep_sequence']
        extracted_data['modified_sequence'] = p_site['modifiedsequence']
        extracted_data['protein_sequence'] = p_site['prot_sequence']
        # PhosPhAt is in Germany and uses commas instead of decimal points
        extracted_data['mass'] = p_site['mass'].replace(",", ".")
        extracted_data['position_in_peptide'] = p_site['position']
        # Call tools.expand_mod_type() to make returned data more comprehensible
        extracted_data['modification_type'] = tools.expand_mod_type(
                p_site['modificationType'])
        print json.dumps(extracted_data) + '\n---'

def list(args):
    raise Exception('Not implemented yet')
