#!/usr/bin/env python

# services.common.tools is a custom module that contains methods shared by
# all four web services.
# The module is located at services/common/tools.py
# Since all four web services are contacting the same remote host (PhosPhAt),
# all code that deals with retrieving the actual data is only written once.
import services.common.tools as tools

# services.common.lists is a custom module that contains lists of valid
# transcripts that PhosPhAt has data on.
# The module is located at services/common/lists.py
# The lists were downloaded from PhosPhAt's website (phosphat.uni-hohenheim.de).
import services.common.lists as lists

# A Python module that allows conversion to and from json.
import json

# 'getExperimentsModAa' is the method used to retrieve experimental data
# from the remote host PhosPhAt. Different methods retrieve different kinds of
# data. We obtained a list of methods that could be called through personal
# communication with PhosPhAt.
API_METHOD = 'getExperimentsModAa'

# Having a search function is required by Adama.
def search(args):
    """Uses PhosPhAt API to return detailed experimental phosphorylation sites
        given a modified peptide sequence.

    Args:
        All arguments are stored in a single dict (args).
        transcript_id: AGI Transcript Identifier. Refers to a specific protein.
            Example value: 'AT1G06410.1'
    """

    # tools.validate_args is a custom method that validates the transcript ID.
    # It will throw an exception if the ID is invalid.
    tools.validate_args(args)

    # tools.request_data is a custom method in the services.common.tools module.
    # It contacts the remote host PhosPhAt and requests phosphorylation data.
    # It returns the data as a dict, which is then stored in phos_sites.
    #
    # tools.request_data accepts two arguments:
    #    - the transcript ID (args['transcript_id'])
    #    - the method used to retrieve experimental data (API_METHOD)
    #
    # args is a dict containing all of the arguments entered by the client,
    # and transcript_id is a field name for a specific argument.
    # All of the field names are specified in the metadata.yml file.
    #
    # This method will raise an exception if it can't connect to PhosPhAt.
    phos_sites = tools.request_data(args['transcript_id'], API_METHOD)

    # The formatting of the data returned was discovered through personal
    # communication with PhosPhAt.
    # phos_sites is a dict, and phos_sites['result'] is a dict within
    # phos_sites. phos_sites['result'] contains the actual data, so
    # that's why we're looping through phos_sites['result'].
    for p_site in phos_sites['result']:
        # Each p_site is a dict within phos_sites['result'].
        extracted_data = {}
        extracted_data['peptide_sequence'] = p_site['pep_sequence']
        extracted_data['modified_sequence'] = p_site['modifiedsequence']
        extracted_data['protein_sequence'] = p_site['prot_sequence']
        # PhosPhAt is in Germany and uses commas instead of decimal points
        extracted_data['mass'] = p_site['mass'].replace(",", ".")
        extracted_data['position_in_peptide'] = p_site['position']
        extracted_data['modification_code'] = p_site['modificationType']
        # Call tools.expand_mod_type to make returned data more comprehensible
        extracted_data['modification_type'] = tools.expand_mod_type(
                p_site['modificationType'])
        # Adama requires JSON objects be printed and separated by three dashes
        print json.dumps(extracted_data) + '\n---'

# Returns a list of valid transcript IDs
def list(args):
    # Prints the list already saved in the lists module
    print json.dumps(lists.EXPERIMENTAL)
