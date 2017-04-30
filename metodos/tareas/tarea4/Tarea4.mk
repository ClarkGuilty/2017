Resultados_hw4.pdf: Resultados_hw4.tex
	pdflatex Resultados_hw4.tex
Resultados_hw4.tex: .txt
	python Plots_Temperatura.py
.txt: heh.exe
	./heh.o
heh.exe: DifusionTemperatura.c
	cc -o heh.o DifusionTemperatura.c -lm