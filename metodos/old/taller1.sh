mkdir taller1
cd taller1
wget https://raw.githubusercontent.com/ComputoCienciasUniandes/HerramientasComputacionalesDatos/master/Homework/hw1/01_notas.tsv
awk '{if($3=="MATEMA" && $4 + $5  + $6 >= 9) print($1, $2, $3, (($4+$5+$6)/3))}' 01_notas.tsv > ja.acevedo12.txt
