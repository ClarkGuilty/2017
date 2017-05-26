all: Resultados_hw5.pdf clean

Resultados_hw5.pdf: canal_ionico.c
	wget https://raw.githubusercontent.com/ClarkGuilty/2017/master/metodos/tareas/datosTarea5/Canal_ionico.txt
	wget https://raw.githubusercontent.com/ClarkGuilty/2017/master/metodos/tareas/datosTarea5/Canal_ionico1.txt
	wget https://raw.githubusercontent.com/ClarkGuilty/2017/master/metodos/tareas/datosTarea5/CircuitoRC.txt
	cc -o canal_ionico.o canal_ionico.c -lm
	-./canal_ionico.o
	python plots_canal_ionico.py
	python circuitoRC.py
	pdflatex Resultados_hw5.tex

clean: 
	-rm -f res1.txt res2.txt g1.png g2.png his1.png his2.png Canal_ionico.txt Canal_ionico1.txt CircuitoRC.txt canal_ionico.o resultados.txt Resultados_hw5.aux Resultados_hw5.log Resultados_hw5.out hisC.png histR.png QT.png RC.png reg.png verC.png verR.png
