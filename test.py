import time

start = time.perf_counter()

time.sleep(3)

end = time.perf_counter()
total_time = end - start
print(total_time)
