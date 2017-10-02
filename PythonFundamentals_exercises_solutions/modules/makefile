
CFLAGS= -Wall -Wextra -std=c99
LDFLAGS= -lcheck

.PHONY: clean

check_dummy: check_dummy.o dummy.o

clean:
	rm -f check_dummy *.o *~

runall: check_dummy
	./check_dummy