import time

def get_time(n):
    start_time = time.time()
    # make my calculations
    result = sum(range(n))
    end_time = time.time()
    print(f'My function took {end_time - start_time: .5f} seconds to run')
    
    return result

print(get_time(100000))
    