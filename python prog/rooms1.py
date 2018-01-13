from sys import stdin, stdout
 
import heapq
 
 
def get_int_array():
    return list(map(int, stdin.readline().split()))
 
 
def solve(N, arrival_times, durations):
 
    departure_times = []
    for i, t in enumerate(arrival_times):
        departure_times.append(t + durations[i])
 
    heapq.heapify(arrival_times)
    heapq.heapify(departure_times)
 
    max_occupancy = 0
    occupancy_count = 0
    while True:
 
        if len(arrival_times) == 0:
            break
 
        if len(departure_times) == 0:
            occupancy_count += len(arrival_times)
            max_occupancy = max(occupancy_count, max_occupancy)
            break
 
        if arrival_times[0] < departure_times[0]:
            heapq.heappop(arrival_times)
            occupancy_count += 1
            max_occupancy = max(occupancy_count, max_occupancy)
            continue
 
        if departure_times[0] <= arrival_times[0]:
            heapq.heappop(departure_times)
            occupancy_count -= 1
            continue
 
    return max_occupancy
 
 
 
T = int(input())
 
for _ in range(T):
    N = int(input())
    arrival_times = get_int_array()
    durations = get_int_array()
 
    print(solve(N, arrival_times, durations))
 
