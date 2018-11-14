from ete3 import EvolTree
from itertools import combinations


tree1 = "((((Lophiola_americana:0.070501,(Dioscorea_elephantipes:0.049471,Tacca_chantrieri:0.059929):0.033181):0.007532,(Xerophyta_retinervis:0.065059,((Pentastemona_sumatrana:0.042806,Stichoneuron_caudatum:0.03634):0.01303,(Freycinetia_banksii:0.021412,Cyclanthus_bipartitus:0.015223):0.009241):0.00832):0.015571):0.003084,((((Petermannia_cirrosa:0.030556,(Wurmbea_pygmaea:0.068777,Alstroemeria_aurea:0.052738):0.033771):0.005818,((Smilax_china:0.05196,(Ripogonum_album:0.015508,Lilium_superbum2:0.064795):0.001092):0.019848,Trillium_luteum:0.072906):0.001269):0.003931,(Campynema_lineare:0.021185,Campynemanthe_viridiflora:0.046804):0.042145):0.011031,(((Asparagus_officinalis:0.036071,Yucca_schidigera:0.028833):0.021143,Iris_missouriensis:0.063696):0.016053,(Cypripedium_formosanum:0.030106,((Sobralia_callosa:0.009884,(Dendrobium_nobile:0.016554,((Cattleya_crispata:0.015453,(Corallorhiza_mertensiana:0.006867,(Corallorhiza_mmaculata:0.001834,Corallorhiza_moccidentalis:0.001423):0.002148):0.042079):0.001791,Cymbidium_tortisepalum:0.02742):0.002341):0.005425):0.003929,Epipactis_mairei:0.0191):0.010214):0.070928):0.00881):0.001783):0.005026,Japonolirion_osense:0.027039);"
taxa = ["Corallorhiza_mertensiana","Corallorhiza_mmaculata","Corallorhiza_moccidentalis"]


t = EvolTree(tree1, format=1)

common_ancestors = []
for taxon in taxa:
    taxon_node = t&taxon
    tID = taxon_node.node_id
    t.mark_tree([tID], ['#1'])


for i in range(len(taxa), 1,-1):
    taxa_groups = [x for x in combinations(taxa, i)]
    for group in taxa_groups:
        common_node = t.get_common_ancestor(*group)

        if(common_node not in common_ancestors):
            common_ancestors.append(common_node)
            
            t.mark_tree([common_node.node_id], ['#1'])

t.write(outfile='testTree.tre')
print(t)










for node in t.traverse():
    if(node.is_leaf()):
        if(node.name in taxa):
            node.name = node.name + "{test}"
    else:
        