#include <stdio.h>

#define max(a, b) (((a) > (b)) ? (a) : (b))

typedef signed char sint8;
typedef unsigned char uint8;
typedef signed short sint16;
typedef unsigned short uint16;
typedef signed int sint32;
typedef unsigned int uint32;
typedef signed long long sint64;
typedef unsigned long long uint64;

sint64 get_max_part_sum(sint32 sequence[], uint64 sequence_len, sint32 pulse)
{
    sint64 max_part_sum = (sequence[0] * pulse);
    sint64 cur_part_sum = max_part_sum;
    pulse *= -1;
    for(uint32 i = 1; i < sequence_len; i++){
        sint64 new_part_sum = cur_part_sum + (sequence[i] * pulse);
        
        // 부분합 업데이트
        cur_part_sum = max(new_part_sum, (sequence[i] * pulse));
        
        // 최댓값 갱신
        max_part_sum = max(max_part_sum, cur_part_sum);

        pulse *= -1;
    }

    return max_part_sum;
}

// sequence_len은 배열 sequence의 길이입니다.
sint64 solution(sint32 sequence[], uint64 sequence_len)
{
    sint64 answer = 0;

    answer = max(get_max_part_sum(sequence, sequence_len, 1), get_max_part_sum(sequence, sequence_len, -1));

    return answer;
}