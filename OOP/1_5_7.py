class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.tr = fr


cp = CPU("INTEL", 16000)


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


me1 = Memory("DDR4", 8)
me2 = Memory("DDR4", 8)


class MotherBoard:
    def __init__(self, name, cpu, **mem_slots):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots[:self.total_mem_slots]

    def get_config(self):
        return [f'Материнская плата: {self.name}',
                f'Центральный процессор: {self.cpu}, {self.cpu.fr}',
                f'Слотов памяти: {self.total_mem_slots}',
                'Память:' + ';'.join(map(lambda x: f'{x.neme}- {x.volom}', self.mem_slots))]


mb = MotherBoard("ASUS", cp, 4, me1, me2)
