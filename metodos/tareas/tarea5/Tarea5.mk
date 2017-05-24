all: resultados.txt clean

resultados.txt: canal_ionico.exe
	./canal_ionico.exe
	python plots_canal_ionico.py

canal_ionico.exe: canal_ionico.c
	gcc -o canal_ionico.exe canal_ionico.c -lm

clean: 
	rm -f res1.txt res2.txt g1.png g2.png his1.png his2.png resultados.txt