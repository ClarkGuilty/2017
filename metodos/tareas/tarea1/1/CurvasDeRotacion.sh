mkdir RotationCurves
cd RotationCurves
wget http://iopscience.iop.org/1538-3881/122/5/2396/fulltext/datafile3.txt
awk '{if($1 == "F571-8")print $0}' datafile3.txt  > a.txt
awk '{$1  = "";print}' a.txt > RotationCurve_F571-8.txt
cp ../PLOTS_RotationCurves.py .
python PLOTS_RotationCurves.py
rm a.txt
rm datafile3.txt
rm PLOTS_RotationCurves.py
































