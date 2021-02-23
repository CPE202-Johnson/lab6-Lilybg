import random
import time

def selection_sort(list):
    comps = 0
    for i in range(len(list)):
        smallest = i
        current = i + 1
        while current < len(list):
            if list[current] < list[smallest]:
                smallest = current
            comps = comps + 1
            current = current + 1
        temp = list[i]
        list[i] = list[smallest]
        list[smallest] = temp
    return comps
  
def insertion_sort(list):
    comps = 0
    i = 1
    while i < len(list): 
        current = list[i] 
        prev = i - 1
        if current > list[prev]:
            comps = comps + 1
        while prev >=0 and current < list[prev] : 
                list[prev+1] = list[prev] 
                prev = prev - 1
                comps = comps + 1
        list[prev + 1] = current
        i = i + 1
    return comps

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of 
    # random numbers is generated at each run
    random.seed(1234) 
    
    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time() 
    #comps = selection_sort(randoms)
    comps = insertion_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__': 
    main()

