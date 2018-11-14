REM requires that all files you want to do this to are in your current working directory

FOR %%i in (*.fasta) DO call C:\Users\klimpert\PhylogeneticsPrograms\mafft-win\mafft.bat --localpair --maxiterate 1000 --adjustdirection --out %%i %%i
