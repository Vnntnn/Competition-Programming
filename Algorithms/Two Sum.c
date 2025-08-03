#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */

// O(n ^ 2) solution => Brute force
// int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
//     int* res = malloc(2 * sizeof(int));
//     *returnSize = 2;

//     for (int i = 0; i < numsSize; i++) {
//         for (int j = i + 1; j < numsSize; j++) {
//             if (nums[i] + nums[j] == target) {
//                 res[0] = i;
//                 res[1] = j;
//                 return res;
//             }
//         }
//     }

//     *returnSize = 0;
//     free(res);
//     return NULL;
// }

// O(n) solution => Hash table
#define HASH_SIZE 20000

typedef struct{
    int value;
    int index;
    int used;
} HashE;

int hashing(int key) {
    return abs(key) % HASH_SIZE;
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    HashE* hash_table = (HashE*)calloc(HASH_SIZE, sizeof(HashE));
    int* res = (int*)malloc(2 * sizeof(int));
    *returnSize = 2;

    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];
        int hash_idx = hashing(complement);

        while (hash_table[hash_idx].used) {
            if (hash_table[hash_idx].value == complement) {
                res[0] = hash_table[hash_idx].index;
                res[1] = i;
                free(hash_table);
                return res;
            }
            hash_idx = (hash_idx + 1) % HASH_SIZE;
        }

        int curr_hash_idx = hashing(nums[i]);
        while(hash_table[hash_idx].used) {
            curr_hash_idx = (curr_hash_idx + 1) % HASH_SIZE;
        }

        hash_table[curr_hash_idx].value = nums[i];
        hash_table[curr_hash_idx].index = i;
        hash_table[curr_hash_idx].used = 1;
    }

    free(hash_table);
    *returnSize = 0;
    return NULL;
}