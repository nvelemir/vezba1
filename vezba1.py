import threading
import time

seconds = 25

def thread_function():
    print("Thread started!")
    start_time= time.time()
    time.sleep(10)
    while True:
        print("hello from thread")
        time.sleep(1)
        current_time = time.time()
        elapsed_time=current_time-start_time
        if(elapsed_time>=seconds):
            break

if __name__ == "__main__":
    x = threading.Thread(target=thread_function)
    x.start()
 
        
        
    
