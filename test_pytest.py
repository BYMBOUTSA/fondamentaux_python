import genetic_mendel

def test_allele_combinations():
    assert genetic_mendel.allele_combinations('RrYy') == ['RY', 'Ry', 'rY', 'ry']
    assert genetic_mendel.allele_combinations("RRYY") == ['RY']
    assert genetic_mendel.allele_combinations("rrYy") == ['rY', 'ry']

def test_genotype_probabilities():
    assert genetic_mendel.genotype_probabilities("RrYy", "RrYy") == {
        'RRYY' : 1 / 16,
        'RRYy' : 2 / 16,
        'RrYY' : 2 / 16,
        'RrYy' : 4 / 16,
        'RRyy' : 1 / 16,
        'Rryy' : 2 / 16,
        'rrYY' : 1 / 16,
        'rryy' : 1 / 16,
        'Rryy' : 2 / 16,
        'rrYY' : 1 / 16,
        'rrYy' : 2 / 16,
        'rryy' : 1 / 16
    }

    def test_most_probable_genotype():
        assert genetic_mendel.most_probable_genotype("RrYy", "RrYy") == "RrYy"