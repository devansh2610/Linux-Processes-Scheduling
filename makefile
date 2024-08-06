all: ans count1 count2 count3

ans: ans.c
	gcc ans.c -o ans

count1: count1.c
	gcc count1.c -o count1

count2: count2.c
	gcc count2.c -o count2

count3: count3.c
	gcc count3.c -o count3

clean:
	rm -f all ans count1 count2 count3
