import heapq
import random

class LoadBalance():
    def __init__(self, worker_num):
        self.worker_num = worker_num
        self.tasks = None
        self.cpu_task_map = [[] for _ in range(self.worker_num)]
        self.cpu_load = [(0,i) for i in range(self.worker_num)]
        # heapq.heapify(self.cpu_load)

    def add_tasks(self, tasks):
        self.tasks = [(time, id) for id, time in enumerate(tasks) ]
        self.tasks.sort(reverse=True)
        print(self.tasks)

    def distribute_task(self):
        for t, id in self.tasks:
            load, cpu = self.get_less_load_cpu()
            self.set_cpu_load((load + t, cpu))
            self.cpu_task_map[cpu].append(id)

    def get_less_load_cpu(self):
        return heapq.heappop(self.cpu_load)

    def set_cpu_load(self, item):
        heapq.heappush(self.cpu_load, item)

    def print_cpu_task_load(self):
        for t_list in self.cpu_task_map:
            print(t_list)

    def print_cpu_time(self):
        for load, cpu in self.cpu_load:
            print(load, cpu)

# 书的答案用的是 job 和 processor 两个类去处理的，就不用额外的数组去对应了

class Job:
    def __init__(self, id, time):
        self.id = id
        self.time = time

    def __lt__(self, other):
        return self.time < other.time


class Processor:
    def __init__(self):
        self.time = 0
        self.job = []

    def add_job(self, job):
        self.time += job.time
        self.job.append(job)

    def __lt__(self, other):
        return self.time < other.time

class LoadBalance2():
    def __init__(self, processor_num):
        self.processor_num = processor_num
        self.processor_heap = [Processor() for i in range(self.processor_num)]
        self.jobs=None

    def add_tasks(self, jobs):
        self.jobs = [Job(id, time) for id, time in enumerate(jobs)]
        self.jobs.sort(reverse=True)

    def distribute_task(self):
        for j in self.jobs:
            min_processor = heapq.heappop(self.processor_heap)
            min_processor.add_job(j)
            heapq.heappush(self.processor_heap, min_processor)

    def print_cpu_task_load(self):
        for p in self.processor_heap:
            print([j.id for j in p.job])

    def print_cpu_time(self):
        for p in self.processor_heap:
            print(p.time)

# 那C一类的该怎么办呢

if __name__ == '__main__':
    tasks = [random.randint(10, 100) for _ in range(30)]
    print(tasks)

    lb = LoadBalance(5)
    lb.add_tasks(tasks)
    lb.distribute_task()
    lb.print_cpu_task_load()
    lb.print_cpu_time()

    print('---------------')

    tasks[-1] = 300
    lb = LoadBalance(5)
    lb.add_tasks(tasks)
    lb.distribute_task()
    lb.print_cpu_task_load()
    lb.print_cpu_time()

    print('---------------')

    lb = LoadBalance2(5)
    lb.add_tasks(tasks)
    lb.distribute_task()
    lb.print_cpu_task_load()
    lb.print_cpu_time()