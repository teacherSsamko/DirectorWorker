import threading
import time
import random


class Worker(threading.Thread):

    def __init__(self, idx):
        super().__init__()
        self.idx = idx
        self.isFinish = False
        self.task = None
    
    def run(self):
        """actual task here"""
        t = 0
        while t < self.task:
            t += 1
            print(f'{self.idx}...{t}/{self.task}')
            time.sleep(0.3)
        self.isFinish = True

class Director:
    def __init__(self, capacity=4):
        self.capacity = capacity
        self.task_to_do = list()
        self.workers = { x : None for x in range(capacity) }

    def check_task(self, task):
        if task % 3 != 0:
            return True
        else:
            print(f'not to do...{task}')
            time.sleep(1)
            return False

    def check_avail_worker(self):
        for worker_idx, status in self.workers.items():
            print(f'worker status\n{worker_idx} - {status}')
            if not status:
                return worker_idx
        print('No avail worker')
        time.sleep(1)
        return False

    def assign_worker(self, worker_idx, task):
        worker = Worker(worker_idx)
        worker.task = task
        self.workers[worker_idx] = worker
        worker.start()
        print(self.task_to_do)

    def check_done_worker(self):
        print("check worker")
        for idx, worker in self.workers.items():
            print(f'worker status in check done {idx} - {worker}')
            if worker and worker.isFinish:
                print(f'worker {worker.idx} finished')
                self.workers[idx] = None
                print(worker)
                # del worker

    def work(self, tasks):
        self.task_to_do = tasks
        while self.task_to_do:
            task = self.task_to_do.pop(0)
            if self.check_task(task):
                while True:
                    worker_idx = self.check_avail_worker()
                    print(worker_idx)
                    if worker_idx is not False:
                        print(f'assign {task} to worker {worker_idx}')
                        self.assign_worker(worker_idx, task)
                        break                      
                self.check_done_worker()
                time.sleep(1)
                


def main():
    tasks = random.sample(range(30), 15)
    print(tasks)
    director = Director(6)
    director.work(tasks)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('forced finish')


