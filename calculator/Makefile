calculator: main.o addition.o subtraction.o multiplication.o division.o
	gcc -o calculator main.o addition.o subtraction.o multiplication.o division.o

main.o: main.c operations.h
	gcc -c main.c

addition.o: addition.c operations.h
	gcc -c addition.c

subtraction.o: subtraction.c operations.h
	gcc -c subtraction.c

multiplication.o: multiplication.c operations.h
	gcc -c multiplication.c

division.o: division.c operations.h
	gcc -c division.c

clean:
	rm -f *.o calculator
