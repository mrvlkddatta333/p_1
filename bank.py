class BankersAlgorithm:
    def __init__(self, allocation, max_resources, available_resources):
        self.allocation = allocation
        self.max_resources = max_resources
        self.available_resources = available_resources
        self.num_processes = len(allocation)
        self.num_resources = len(available_resources)

    def is_safe_state(self):
        work = self.available_resources.copy()
        finish = [False] * self.num_processes
        safe_sequence = []

        for _ in range(self.num_processes):
            for process in range(self.num_processes):
                if not finish[process]:
                    if all(
                        work[i] >= self.max_resources[process][i] - self.allocation[process][i]
                        for i in range(self.num_resources)
                    ):
                        safe_sequence.append(process)
                        work = [
                            work[i] + self.allocation[process][i]
                            for i in range(self.num_resources)
                        ]
                        finish[process] = True
                        break

        if all(finish):
            print("Safe Sequence:", safe_sequence)
            return True
        else:
            print("Unsafe State")
            return False
    
        

allocation_matrix = [
 [0, 1, 0],
 [2, 0, 0],
 [3, 0, 2],
 [2, 1, 1],
 [0, 0, 2]
]
max_matrix = [
 [7, 5, 3],
 [3, 2, 2],
 [9, 0, 2],
 [2, 2, 2],
 [9, 3, 3]
]
available_resources_vector = [3, 3, 2]
banker = BankersAlgorithm(allocation_matrix, max_matrix, available_resources_vector)
banker.is_safe_state()