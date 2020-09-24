def proteins(strand):
    codons_proteins_dict = {
    'AUG': 'Methionine',
    'UUU': 'Phenylalanine',
    'UUC': 'Phenylalanine',
    'UUA': 'Leucine',
    'UUG': 'Leucine',
    'UCU': 'Serine',
    'UCC': 'Serine',
    'UCA': 'Serine',
    'UCG': 'Serine',
    'UAU': 'Tyrosine',
    'UAC': 'Tyrosine',
    'UGU': 'Cysteine',
    'UGC': 'Cysteine',
    'UGG': 'Tryptophan',
    'UAA': 'STOP',
    'UAG': 'STOP',
    'UGA': 'STOP'
    }
    codons = [strand[i-3:i] for i in range(3, len(strand)+3, 3)]
    proteins = []
    for codon in codons:
        protein = codons_proteins_dict.get(codon)
        if not protein or protein == 'STOP':
            return proteins
        proteins.append(protein)
    return proteins