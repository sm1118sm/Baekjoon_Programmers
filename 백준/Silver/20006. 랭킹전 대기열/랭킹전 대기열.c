#include <stdio.h>
#include <string.h>

int main() {
    int p, m;
    int level[300];
    int room[300][300];
    char name[300][17];
    int room_count = 0
    int room_size[300] = {0};

    // 입력 받기
    scanf("%d %d", &p, &m);
    for (int i = 0; i < p; i++) {
        scanf("%d %s", &level[i], name[i], 17);
    }

    // 플레이어 입장 처리
    for (int i = 0; i < p; i++) {
        int placed = 0;
        for (int j = 0; j < room_count; j++) {
            if (room_size[j] < m && level[room[j][0]] - 10 <= level[i] && level[i] <= level[room[j][0]] + 10) {
                room[j][room_size[j]++] = i;
                placed = 1;
                break;
            }
        }
        if (!placed && room_count < 300) {
            room[room_count][0] = i;
            room_size[room_count++] = 1;
        }
    }

    // 출력
    for (int i = 0; i < room_count; i++) {
        if (room_size[i] == m) {
            printf("Started!\n");
        } else {
            printf("Waiting!\n");
        }

        // 닉네임 정렬 (삽입 정렬 사용)
        for (int j = 1; j < room_size[i]; j++) {
            for (int k = j; k > 0 && strcmp(name[room[i][k - 1]], name[room[i][k]]) > 0; k--) {
                int temp = room[i][k];
                room[i][k] = room[i][k - 1];
                room[i][k - 1] = temp;
            }
        }

        // 플레이어 출력
        for (int j = 0; j < room_size[i]; j++) {
            int player_index = room[i][j];
            printf("%d %s\n", level[player_index], name[player_index]);
        }
    }
    return 0;
}
