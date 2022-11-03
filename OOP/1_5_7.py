class CPU:
    def __init__(self, name, clock_frequency):
        self.name = name
        self.tr = clock_frequency


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, total_mem_slots=4, **mem_slots):
        self.name = name
        CPU = cpu
