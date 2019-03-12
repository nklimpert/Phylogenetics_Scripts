REM requires that all files you want to do this to are in your current working directory

FOR %%i in (*.fasta) DO call C:\Users\klimpert\PhylogeneticsPrograms\iqtree-1.6.5-Windows\bin\iqtree.exe -s %%i 
