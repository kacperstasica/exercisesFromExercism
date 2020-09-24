def check_if_match(codon, list_of_codons):
    '''
    This function converts string of codons (e.g. 'UAA, UUG') into list of codons
    and then it checks if any element in that list matches the list of codons
    (the RNA turned into list)
    '''
    codons_in = codon.split(', ')
    return any(item in codons_in for item in list_of_codons)

def check_position(list_of_proteins, list_of_codons):
    check_uaa = any(i in ['UAA'] for i in list_of_codons)
    if check_uaa:
        return list_of_proteins[:list_of_codons.index('UAA')]
    check_uag = any(i in ['UAG'] for i in list_of_codons)
    if check_uag:
        return list_of_proteins[:list_of_codons.index('UAG')]
    check_uga = any(i in ['UGA'] for i in list_of_codons)
    if check_uga:
        return list_of_proteins[:list_of_codons.index('UGA')]
    return list_of_proteins


def proteins(strand):
    # generates the list of codons e.g. ["AUG", "UUU", "UCU", "UAA", "AUG"]
    codons = [strand[i-3:i] for i in range(3, len(strand)+3, 3)]
    proteins = []
    if check_if_match('AUG', codons):
        proteins.append('Methionine')
    if check_if_match('UUU, UUC', codons):
        proteins.append('Phenylalanine')
    if check_if_match('UUA, UUG', codons):
        proteins.append('Leucine')
    if check_if_match('UCU, UCC, UCA, UCG', codons):
        proteins.append('Serine')
    if check_if_match('UAU, UAC', codons):
        proteins.append('Tyrosine')
    if check_if_match('UGU, UGC', codons):
        proteins.append('Cysteine')
    if check_if_match('UGG', codons):
        proteins.append('Tryptophan')
    if check_if_match('UAA, UAG, UGA', codons):
        return check_position(proteins, codons)
    return proteins
