"""strips out files anything besides the gentianales"""



from Bio import SeqIO
import os, sys

GENTIANALES = {"Bartonia_virginica", "Exacum_affine", "Obolaria_virginica", "Voyria_clavata","Exochaenium_oliganthum", "Voyria_caerulea", "Coffea_arabica", "Pentalinon_luteum", "Echiles_umbellatus", "Asclepias_syrica", "Nerium_oleander", "Rhazya_stricta", "Catharanthus_roseus", "Oncinotis_tenuiloba" }
FASFORMAT = {".fasta", ".fas", ".FNA", ".fa"}



for file in os.listdir():
    if os.path.splitext(file)[-1] == ".fasta":
        with open(file.replace("alltaxa", "gentianales"), 'w') as outFile:
            for seq in SeqIO.parse(file, "fasta"):
                if seq.id in GENTIANALES:
                    outFile.write(seq.format("fasta"))

print("Done!")