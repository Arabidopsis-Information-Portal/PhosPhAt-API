#!/usr/bin/env python
import services.common.tools as tools # Custom module for shared functions
import json # Allows conversion to and from json

# Specify kind of data to retrieve from PhosPhAt
API_METHOD = 'getExperimentsModAa'

# search function is required by Adama
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

    # phos_sites['result'] refers to a dict in phos_sites that has the data
    for p_site in phos_sites['result']:
        extracted_data = {}
        extracted_data['peptide_sequence'] = p_site['pep_sequence']
        extracted_data['modified_sequence'] = p_site['modifiedsequence']
        extracted_data['protein_sequence'] = p_site['prot_sequence']
        # PhosPhAt is in Germany and uses commas instead of decimal points
        extracted_data['mass'] = p_site['mass'].replace(",", ".")
        extracted_data['position_in_peptide'] = p_site['position']
        extracted_data['modification_code'] = p_site['modificationType']
        # Call tools.expand_mod_type() to make returned data more comprehensible
        extracted_data['modification_type'] = tools.expand_mod_type(
                p_site['modificationType'])
        # Adama requires JSON objects be separated by three dashes
        print json.dumps(extracted_data) + '\n---'

# Returns a list of valid transcript IDs
def list(args):
    with open('services/phosphorylated_experimental/experimental_transcripts.txt') as f:
        valid_transcripts = f.readlines()
    print json.dumps(valid_transcripts)
