#!/usr/bin/env python3

import Bio
from Bio import AlignIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import generic_dna

import os


fullTaxonSet = {"Pogoniopsis_sp", "Apostasia_sp", "Pogonia_ophioglossoides", "Phragmipedium_longifolium", "Codonorchis_lessonii", "Aa_palacea", "Thelymitra_cyanea", "Dactilorhiza", "Palmorchis_pabstii", "Nervilia_crociformis", "Triphora_trianthophora", "Tropidia_polystachya", "Sobralia_callosa", "Coelogyne_flaccida", "Phaius_tankervillieae", "Calanthe_triplicata", "Cymbidium_aloifolium", "Calypso_bulbosa", "Coelia_triptera", "Cattleya_aurantiaca", "Phalaenopsis_equestris", "Angraecum_sesquipedale", "Earina_autumnalis", "Liparis_loeselii", "Dendrobium_huoshanense", "Asparagus_officinalis"}

#main directory where all the files are
maindir = os.getcwd()

#  loops over each
for root, dirs, files in os.walk(maindir):
    #  files are only those with the fasta extension in the cwd
    for file in filter(lambda x: x.endswith('.fasta'), files):
        alignment = AlignIO.read(os.path.join(root, file), "fasta")

        #  makes a set of all the names of taxa in the alignment
        taxa = set(record.id for record in alignment)

        #  how long each sequence is in the alignment
        seqLength = alignment.get_alignment_length()

        #  the sequences that are missing from the alignment
        missingSeqs = fullTaxonSet - taxa

        #  only do this if there are missing sequences
        for taxon in missingSeqs:
            #  make a dummy sequence of the right length
            dummy = SeqRecord(Seq(seqLength*'N', generic_dna), id=taxon, name=taxon)
            alignment.append(dummy)

        #  at this point, alignment should be filled, so it can be rewritten
        with open(os.path.join(root,file), 'w') as outFile:
            outFile.write(alignment.format("fasta"))
