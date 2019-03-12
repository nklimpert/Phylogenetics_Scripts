REM treeAnnotator bat

for %%i in (*.trees) do call C:\Users\klimpert\PhylogeneticsPrograms\BEASTv1.8.3\bin\treeannotator.cmd -heights mean -burnin 5000000 %%i %%iout.txt
