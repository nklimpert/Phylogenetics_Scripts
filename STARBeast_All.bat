REM run beast from the command line on every .xml file in the current working directory

FOR %%i in (*.xml) DO call java -jar C:\Users\klimpert\PhylogeneticsPrograms\BEAST2\lib\beast.jar -beagle -overwrite -errors 0 -threads 2 %%i
