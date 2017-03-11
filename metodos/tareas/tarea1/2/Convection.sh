mkdir Convection
cd Convection
cp ../DatosRadioSonda.dat .
awk '{if(NR>3 && $2 > 1500 )print $2,$3}' DatosRadioSonda.dat > TempHeight.txt
cp ../PLOTS_Convection.py .
python PLOTS_Convection.py
rm PLOTS_Convection.py


