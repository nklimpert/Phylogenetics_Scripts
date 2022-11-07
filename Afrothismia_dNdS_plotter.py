#!/usr/bin/env python3.10
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/home/klimpert/Documents/research/Afrothismia/figures/dNdS/dnds_data_20221104.csv")



AFGE_paml = df[["Gene", "AFGE_bg", "AFGE_fg"]]
AFHY_paml = df[["Gene", "AFHY_bg", "AFHY_fg"]]
AFWI_paml = df[["Gene", "AFWI_bg", "AFWI_fg"]]
AFGE_relax = df[["Gene", "AFGE_relax"]]
AFHY_relax = df[["Gene", "AFHY_relax"]]
AFWI_relax = df[["Gene", "AFWI_relax"]]


fig, axes = plt.subplots(nrows=3, ncols=2, sharex=True)

AFGE_paml.plot.bar(ax=axes[0,0], x='Gene', ylim=(0,0.5), ylabel="dN/dS")
AFGE_relax.plot.bar(ax=axes[0,1], x='Gene', ylim=(0,2.5), ylabel="k-value")
AFHY_paml.plot.bar(ax=axes[1,0], x='Gene', ylim=(0,0.5), ylabel="dN/dS")
AFHY_relax.plot.bar(ax=axes[1,1], x='Gene', ylim=(0,2.5), ylabel="k-value")
AFWI_paml.plot.bar(ax=axes[2,0], x='Gene', ylim=(0,0.5), ylabel="dN/dS")
AFWI_relax.plot.bar(ax=axes[2,1], x='Gene', ylim=(0,2.5), ylabel="k-value")

axes[0,1].axhline(y=1.0, color='grey', linestyle='--')
axes[1,1].axhline(y=1.0, color='grey', linestyle='--')
axes[2,1].axhline(y=1.0, color='grey', linestyle='--')

plt.show()