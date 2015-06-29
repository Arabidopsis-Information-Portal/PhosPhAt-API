import json

# Returns the expanded form of the modification type
def expand_mod_type(short_version):
    switcher = {
        'phos' : 'experimental/validated phosphorylation site',
        'phos_amb' : 'ambiguous phosphorylation site',
        'ox' : 'site of oxidized methionine'
    }
    return switcher.get(short_version, 'unknown')

# Performs an experimental search.
def experimental(phos_sites, MOD_SEQ):

    current_data = {}
    if MOD_SEQ is not None:
        for p_site in phos_sites['result']:
            # Print data from p_sites with the given modified sequence
            if MOD_SEQ == p_site['modifiedsequence']:
                current_data.clear()
                current_data['affected_amino_acid'] = p_site['affectedAminoacid']
                current_data['position_in_protein'] = p_site['position']
                current_data['peptide_sequence'] = p_site['pep_sequence']
                current_data['modification_type'] = expand_mod_type(p_site['modificationType'])
                print json.dumps(current_data) + '\n---'
    else:
        # Save all sequences for given transcript
        mod_seqs = []
        for p_site in phos_sites['result']:
            mod_seqs.append(p_site['modifiedsequence'].strip())

        # Print all unique sequences
        mod_seqs = set(mod_seqs)
        for seq in mod_seqs:
            current_data.clear()
            current_data['modified_sequence'] = seq
            print json.dumps(current_data) + '\n---'


def predicted(phos_sites):
    current_data = {}
    # 13mer gives a 13char amino acid sequence, and the affected amino
    # acid is always the 7th character.
    amino_acid_loc = 6

    for p_site in phos_sites['result']:
        current_data['position_in_protein'] = p_site['prd_position']
        current_data['prediction_score'] = p_site['prd_score']
        current_data['13mer_sequence'] = p_site['prd_13mer']
        current_data['affected_amino_acid'] = p_site['prd_13mer'][amino_acid_loc]
        print json.dumps(current_data) + '\n---'

def hotspot(phos_sites):
    current_data = {}
    # Print hotspot data
    for p_site in phos_sites['result']:
        current_data['hotspot_sequence'] = p_site['hsp_hotspot_sequenz']
        current_data['start_position'] = p_site['hsp_hotspot_start']
        current_data['end_position'] = p_site['hsp_hotspot_stop']
        print json.dumps(current_data) + '\n---'
