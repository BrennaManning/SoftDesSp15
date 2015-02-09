# -*- coding: utf-8 -*-
"""
Created on Sat Jan  31 8:24:42 2015

@author: Brenna Manning

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq


def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###
def  collapse(L):
    output = ""
    for s in L:
        output = output + s
    return output

def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide

    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
        """
    #complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    #new_sequence.append(complements[nucleotide])

    if nucleotide == 'A':
        n_complement = 'T'
    elif nucleotide == 'T':
        n_complement ='A'
    elif nucleotide == 'C':
        n_complement = 'G'
    elif nucleotide == 'G':
        n_complement = 'C'

    return n_complement



    # TODO: implement this

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence

        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """
    # TODO: implement this

    dna_dict = {'A':'T','T':'A','G':'C','C':'G'}

    return "".join([dna_dict[base] for base in reversed(dna)])


def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.

        stop codons are TAG TAA and TGA

        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    """
    # TODO: implement this

    #stop_codons = ['TAG','TAA','TGA']
    #odon = orf[i:i+3] ????????????

    ORF = '' # it's a string

    i = 0
    while i < (len(dna)): #length of dna/3 is how many codons - makes it so there are as many iterations through loops as there are codons
        codon_first = i #every multiple of 3 is the start of a codon
        codon_last = i+3 #add three to get the third entry of codon - (originally expected +2 but that only returned 2 letters for a codon??)
        codon = dna[codon_first:codon_last]
        #print codon

        if codon in ['TAG', 'TAA', 'TGA']: #end codon
            return dna[0:i]

        i += 3
            #ORF = ORF + codon #next codon is added to string if it is not an end codon
    return dna


        #if codon_first_char == 'T' and codon_mid_char == 'A' and codon_last_char == 'G' or 'A':
        #    break
        #elif codon_first_char == 'T' and codon_mid_char == 'G' and codon_last_char == 'A':
        #    break
        #else
        #????

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
        test was incorrect - changed expected values
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    # TODO: implement this

    start_codon = 'ATG'
    # stop_codon = 'TAG' or 'TGA' or 'TAA'

    ORF = '' # it's a string?

    ORFS_oneframe = []
    i = 0
    while i  < len(dna):
        codon_first = i
        codon_last = i+3 #add three to get the third entry of codon
        codon = dna[codon_first:codon_last]
        if codon == start_codon:
            ORF = rest_of_ORF(dna[i:])
            ORFS_oneframe.append(ORF)
            i += len(ORF)
        else:
            i += 3

    return ORFS_oneframe

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """


    # TODO: implement this
    all_ORFS = []

    # All_Frames_ORFs = collapse(find_all_ORFs_oneframe(dna[0:2]))
   #frame1ORFS = collapse(find_all_ORFs_oneframe(dna))
    #frame2ORFS = collapse(find_all_ORFs_oneframe(dna[1:]))#start with 2nd character in string
    #frame3ORFS = collapse(find_all_ORFs_oneframe(dna[2:]))#start with 3rd character in string

    for i in range(3):
        current_frame = dna[i:]
        All_Frames_ORFs = find_all_ORFs_oneframe(current_frame)
        if len(All_Frames_ORFs) > 1:
        #     print "appending to all_orfs"
            all_ORFS.extend(All_Frames_ORFs)
   #all_ORFS.append(frame1ORFS)
    #all_ORFS.append(frame2ORFS)
    #all_ORFS.append(frame3ORFS)
    return all_ORFS





def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    # TODO: implement this

    dna2 = get_reverse_complement(dna)


    all_ORFS_Both = find_all_ORFs(dna)
    all_ORFS_Both.extend(find_all_ORFs(dna2))

    #print all_ORFS_Both
    return all_ORFS_Both

    #returns list of strings



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    orfs=find_all_ORFs_both_strands(dna)
    long_orf=orfs[0]
    for frame in orfs:
        if len(frame)>len(long_orf):
            long_orf=frame
    return long_orf

    # # TODO: implement this

    # longest_orf = max(find_all_ORFs_both_strands(dna), key=len)
    # # print "in longest_orf", len(longest_orf)
    # return longest_orf



def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence

        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    # TODO: implement this
    strand = ""
    maxlen = 0
    for i in range(num_trials):
        strand_len = len(longest_ORF(shuffle_string(dna)))
        if strand_len > maxlen:
            maxlen = strand_len
            print "rewriting longest_orf"
    return maxlen



def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).

        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    # TODO: implement this
    a_acids = "" #string!
    codons = [] #list!

    for i in range(0, len(dna) -2, 3):
        codons.append(dna[i:i+3])
    a_acids = "".join(aa_table[i] for i in codons)
    return a_acids


def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.

        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    # TODO: implement this

    return [coding_strand_to_AA(i) for i in find_all_ORFs_both_strands(dna) if len(i) >= threshold]
#    for i in find_all_ORFs_both_strands(dna)
 #       if len(i) >= threshold
  #      amino_acid_sequences = coding_strand_to_AA(i)
   #     return amino_acid_sequences



dna = load_seq("./data/X73525.fa")
threshold = longest_ORF_noncoding(dna, 1500)
print threshold
amino_acids =  gene_finder(dna, threshold)
print amino_acids

# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()