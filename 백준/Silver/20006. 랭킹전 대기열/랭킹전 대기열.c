#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
	int hostLevel;
	int count;
	int person[300];
}room;

int p, m, roomCount = 0, roomNum, level[300];

room rooms[300];

char name[300][17];

int compare(const void* f, const void* s) {
    return strcmp(name[*((int*)f)], name[*((int*)s)]); 
}

int abs(int a) { 
    return a < 0 ? -a : a; 
}

int main() {
	scanf("%d %d", &p, &m);
    
	for (int i = 0; i < p; i++) {
		scanf("%d %s", &level[i], name[i]);

		//방 정해주기
		roomNum = -1;
        
		for (int j = 0; j < roomCount; j++){
            if (abs(rooms[j].hostLevel - level[i]) <= 10 && rooms[j].count < m) { 
                roomNum = j; 
                break; 
            }
        }
		//방에 넣어주기
		if (roomNum == -1) {
			roomNum = roomCount++;
			rooms[roomNum].hostLevel = level[i];
			rooms[roomNum].person[0] = i;
			rooms[roomNum].count = 1;
		}
        
		else rooms[roomNum].person[rooms[roomNum].count++] = i;
	}

	for (int i = 0; i < roomCount; i++) {
		if (rooms[i].count == m){
            printf("Started!\n");
        }
        
		else {
            printf("Waiting!\n");
        } 
        
		qsort(rooms[i].person, rooms[i].count, sizeof(int), compare);
        
		for (int j = 0; j < rooms[i].count; j++){
            printf("%d %s\n", level[rooms[i].person[j]], name[rooms[i].person[j]]);
        }
	}
	return 0;
}
