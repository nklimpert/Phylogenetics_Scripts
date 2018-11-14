REM fasttree batch file

FOR %%i in (*.FNA) DO call fasttree -gtr -nt %%i > %%i~ni.tre
