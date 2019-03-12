#!/usr/bin/env python
'''Replaces all names in a text file with their real names.'''
import sys

names = {'DALT': 'D_alata1*',
            'SRR3938623': 'D_alata2*',
            'P09': 'D_calcicola',
            'P32': 'D_nummularia',
            'SRR3938611': 'D_rotundata*',
            'P26': 'D_mayottensis',
            'P27': 'D_hombuka',
            'DISO13': 'D_soso*',
            'P25': 'D_sansibarensis',
            'DIPE13': 'D_cochleariapiculata*',
            'P29': 'D_pentaphylla',
            'P28': 'D_antaly',
            'SRR3938635': 'D_trifida*',
            'P30': 'D_cordata',
            'P05': 'D_birmanica',
            'P04': 'D_daunea',
            'P31': 'D_pseudonitens',
            'DVIT': 'D_villosa*',
            'DISY13': 'D_sylvatica*',
            'P03': 'D_kituiensis',
            'DICO13': 'D_communis*',
            'P06': 'D_communis',
            'P18': 'D_tentaculigera',
            'P02': 'D_calcencis',
            'P23': 'D_monandra',
            'P24': 'D_campestris',
            'P21': 'D_pohlii',
            'P22': 'D_orthogoneura',
            'DCOT': 'D_composita*',
            'P20': 'D_minima',
            'SRR1218151': 'D_zingiberensis*',
            'P10': 'D_caucasica',
            'SRR5457049': 'D_nipponica*',
            'P01': 'D_rockii',
            'P08': 'D_membranacea',
            'P07': 'D_prazeri',
            'TACT': 'Tacca_chantrieri*',
            'P17': 'Trichopus_zeylanicus',
            'W25': 'Burmannia_bicolor',
            'W26': 'Gymnosiphon_longistylus',
            'W28': 'Apteria_aphylla',
            'DIPE1_3': 'D_cochleariapiculata*',
            'DICO1_3': 'D_communis*',
            'DISY1_3': 'D_sylvatica*',
            'DISO1_3': 'D_soso*',
			'DIPE1': 'D_cochleariapiculata*',
            'DICO1': 'D_communis*',
            'DISY1': 'D_sylvatica*',
            'DISO1': 'D_soso*',
            'D01': 'Burmannia_bicolor1',
            'D02': 'Burmannia_juncea',
            'D06': 'Burmannia_itoana',
            'D14': 'Burmannia_championii',
            'D24': 'Burmannia_longifolia1',
            'D25': 'Burmannia_longifolia2',
            'D26': 'Burmannia_madagascariensis',
            'D36': 'Burmannia_bicolor2',
            'D03': 'Miersiella_umbelata',
            'D04': 'Gymnosiphon_longistylus1',
            'D09': 'Apteria_aphylla1',
            'D10': 'Dictyostega_orobanchoides1',
            'D11': 'Gymnosiphon_divaricatus',
            'D12': 'Apteria_aphylla2',
            'D20': 'Campylosiphon_purpurascens',
            'D21': 'Hexapterella_gentianoides',
            'D23': 'Dictyostega_orobanchoides2',
            'D27': 'Gymnosiphon_constrictus',
            'D28': 'Oxygyne_yamashitae',
            'D35': 'Gymnosiphon_longistylus2',
            'D05': 'Aletris_lutea',
            'D08': 'Lophiola_aura',
            'D13': 'Narthecium_ossifragum',
            'D17': 'Narthecium_californicum',
            'D18': 'Nietneria_paniculata',
            'D31': 'Metanarthecium_luteoviride1',
            'D32': 'Metanarthecium_luteoviride2',
            'D07': 'Afrothismia_hydra',
            'D15': 'Thismia_rodwayi',
            'D16': 'Thismia_javanica',
            'D19': 'Thismia_panamensis',
            'D22': 'Afrothismia_winkleri',
            'D29': 'Freycinetia_arborea1',
            'D30': 'Freycinetia_arborea2',
            'D33': 'Barbacenia_boliviensis1',
            'D34': 'Barbacenia_boliviensis2',
            'D37': 'Cyclanthus_bipartitus',
            'D38': 'Pandanus_aff_parva',
            'D39': 'Japonolirion_osense',
            'D40': 'Stemona_tuberosa',
            'D41': 'Pentastemona_sumatrana',
            'D42': 'Sciaphila_densiflora',
            'D43': 'Apteria_aphylla3'
            }

info = ''

inFile = sys.argv[1]
with open(inFile, 'r') as data:
    info = data.read()

for key, value in names.items():
    if key in info:

        info = info.replace(key, value)

with open(inFile, 'w') as rewrite:
    rewrite.write(info)
