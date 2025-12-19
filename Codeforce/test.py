
# class Attraction:
#     def __init__(self, name, time, rating):
#         self.name = name
#         self.time = time
#         self.rating = rating
#     def get_name(self):
#         return self.name
#     def get_time(self):
#         return self.time
#     def get_rating(self):
#         return self.rating
#     def get_cost(self):
#         return self.rating/self.time

# def travel(attractions, days):
#     sorted_attractions = sorted(attractions, key=lambda a: a.get_cost(), reverse=True)

#     total_rating = 0
#     total_time = 0
#     selected = []

#     for attraction in sorted_attractions:
#         if total_time + attraction.get_time() <= days:
#             total_time += attraction.get_time()
#             total_rating += attraction.get_rating()
#             selected.append(attraction)

#     if not selected:
#         print("Cannot travel in the given days.")
#     else:
#         for attraction in selected:
#             print(f"{attraction.get_name()} -> {attraction.get_time()} day(s) -> {attraction.get_rating()} scores")
#         print(f"Total rating: {total_rating} scores")

# def main():
#     import json
#     attractions = []
#     num_attractions = int(input())
#     while num_attractions != 0:
#         attraction_in = json.loads(input())
#         attractions.append(Attraction(attraction_in['name'], attraction_in['time'], attraction_in['rating']))
#         num_attractions = num_attractions - 1
#     days = float(input())
#     print("==== Results ====")
#     travel(attractions, days)

# main()

# class ProbHash:
#     def __init__(self, size, rehash_size):
#         self.hash_table = [None] * size
#         self.size = size
#         self.rehash_size = rehash_size
    
#     def insert_data(self, subj_id):
#         hash_index = subj_id % self.size
#         original_index = hash_index
        
#         while self.hash_table[hash_index] is not None:
#             hash_index = (hash_index + self.rehash_size) % self.size
#             if hash_index == original_index:
#                 return

#         self.hash_table[hash_index] = subj_id
#         print(f"Insert {subj_id} at index {hash_index}")
    
#     def search_data(self, subj_id):
#         hash_index = subj_id % self.size
#         original_index = hash_index
        
#         while self.hash_table[hash_index] is not None:
#             if self.hash_table[hash_index] == subj_id:
#                 print(f"Found {subj_id} at index {hash_index}")
#                 return
#             hash_index = (hash_index + self.rehash_size) % self.size
#             if hash_index == original_index:
#                 break

#         print(f"Sorry, {subj_id} does not exist.")
    
#     def print_hashtable(self):
#         print(self.hash_table)

# def main():
#     import json
#     size = int(input())
#     rehash_size = int(input())
#     hashtable = ProbHash(size, rehash_size)
#     while True:
#         finish = input()
#         if finish == "Done":
#             break
#         condition, data = finish.split(" = ")
#         if condition == "I":
#             hashtable.insert_data(int(data))
#             print("------")
#         elif condition == "S":
#             hashtable.search_data(int(data))
#             print("------")
#         elif condition == "P":
#             hashtable.print_hashtable()
#             print("------")
#         else:
#             print("Invalid Condition!")
# main()

# def lcs(str1, str2):
#     m, n = len(str1), len(str2)
#     dp = [[0]*(n+1) for _ in range(m+1)]
#     for i in range(1, m+1):
#         for j in range(1, n+1):
#             if str1[i-1] == str2[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#     if dp[m][n] == 0:
#         print("No common subsequence.")
#     else:
#         print(dp[m][n])

# def main():
#     str1 = input()
#     str2 = input()
#     lcs(str1, str2)

# main()


def sort_exam(lst):
    """
    """
    if not lst:
        return lst

    max_len = 0
    min_len = 1000000
    for s in lst:
        l = len(s)
        if l > max_len:
            max_len = l
        if l < min_len:
            min_len = l

    buckets = [[] for _ in range(max_len - min_len + 1)]
    for s in lst:
        buckets[max_len - len(s)].append(s)

    def radix_radix_desc(strings, length):
        for pos in range(length-1, -1, -1):
            count = [[] for _ in range(256)]
            for s in strings:
                count[ord(s[pos])].append(s)
            strings = []
            for c in range(255, -1, -1):
                strings.extend(count[c])
        return strings

    result_lst = []
    for bucket in buckets:
        if bucket:
            l = len(bucket[0])
            bucket_result = radix_radix_desc(bucket, l)
            result_lst.extend(bucket_result)

    if result_lst == lst:
        return "Given list is already sorted from the beginning."
    return result_lst

def main():
    import json
    print(sort_exam(json.loads(input())))
main()


"""


Basic sorting (Insrtion base)
Time complexity: O(n^2 * m)
Space complexity: O(1) + in-place


"""
# def sort_exam(list: list) -> list:
#     """Insertion sorting"""
#     compare = 0

#     for current in range(len(list)):
#         biggest = current
#         walker = current

#         while walker < len(list):
#             if len(list[walker]) > len(list[biggest]) or (len(list[walker]) == len(list[biggest]) and list[walker][0:] > list[biggest][0:]):
#                 biggest = walker
#                 compare += 1
#             walker += 1

#         list[current], list[biggest] = list[biggest] ,list[current]
    
#     if not compare:
#         return "Given list is already sorted from the beginning."

#     return list

# def main():
#     """Main Function"""
#     import json
#     print(sort_exam(json.loads(input())))
# main()

"""


Counting and Radix sorting
Time complexity: O(n * m)
Space complexity: O(n + m)


"""
def sort_exam(lst):
    """
    Sort function
    """
    if not lst:
        return lst

    max_len = 0
    min_len = 1000000
    for s in lst:
        l = len(s)
        if l > max_len:
            max_len = l
        if l < min_len:
            min_len = l

    buckets = [[] for _ in range(max_len - min_len + 1)]
    for s in lst:
        buckets[max_len - len(s)].append(s)

    def radix_sorrt_desc(strings, length):
        for pos in range(length-1, -1, -1):
            count = [[] for _ in range(256)]
            for s in strings:
                count[ord(s[pos])].append(s)
            strings = []
            for c in range(255, -1, -1):
                strings.extend(count[c])
        return strings

    sorrtedd_lst = []
    for bucket in buckets:
        if bucket:
            l = len(bucket[0])
            sorrtedd_bucket = radix_sorrt_desc(bucket, l)
            sorrtedd_lst.extend(sorted_bucket)

    if sorrtedd_lst == lst:
        return "Given list is already sorted from the beginning."
    return sorrtedd_lst

def main():
    """
    Main function
    """
    import json
    print(sort_exam(json.loads(input())))
main()
