#Heh
.PHONY: heh
heh :
	cc main.c
	./a.out
	python histo.py
	git add main.c
	git add histo.py
	git add rand.png
	git commit -m "Makefile actualiz� los archivos"
	git push