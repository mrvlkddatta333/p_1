import random
import time
from threading import Thread, Lock

num_processes = 5

class Process:
    def __init__(self,pid):
        self.pid = pid
        self.is_leader = False
        self.lock = Lock()

    def run(self):
        
        time.sleep(random.uniform(0.1,0.5))

        next_process = (self.pid+1) % num_processes
        with processes[next_process].lock:
            if not processes[next_process].is_leader:
                print(f"Process {self.pid} sends a message to Process {next_process}")
            
            if self.pid==max(p.pid for p in processes):
                self.is_leader = True
                print(f"Process {self.pid} becomes the leader")


processes = [Process(pid) for pid in range(num_processes)]
threads = [Thread(target=p.run) for p in processes]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

leader = [p for p in processes if p.is_leader][0]
print(f"Leader is Process {leader.pid}")