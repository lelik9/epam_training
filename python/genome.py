import argparse
# import re
import regex as re
import io

from datetime import datetime
from multiprocessing import Process, Queue


class Parser(Process):
    """
    Proccess worker for parsing
    """
    def __init__(self, queue, pattern):
        super(Parser, self).__init__()
        self.queue = queue
        self.pattern = pattern

    def run(self):
        while True:
            msg = self.queue.get()
            if isinstance(msg, dict):
                self.parse(msg['line'], msg['out'])
            elif isinstance(msg, str) and msg == 'quit':
                break

    def parse(self, line, out):
        # out = 'c:\\'+out
        with open(out, 'w') as f:
            for m in re.finditer(self.pattern, line, overlapped=True):
                f.write('Posttion: {}; Line: {}'.format(m.start(), m.group(0)))


def genereate_rgex(pattern) -> str:
    """
    Generating regexp for searching from entered pattern
    :return: regexp pattern: str
    """
    match_acid = {
        'A':'RMWDHV',
        'C':'YMSBHV',
        'G':'RKSBDV',
        'T':'YKWBDH',
        'U':'YKWBDH'
    }
    lst = []
    pattern = pattern.replace('N', '.')

    for char in pattern:
        if char != '.':
            lst.append('[{}{}N]'.format(char, match_acid.get(char,'')))
        else:
            lst.append('{}'.format(char))

    pattern = ''.join(lst)

    return pattern


def build_worker_pool(queue, size, pattern):
    workers = []
    for _ in range(size):
        worker = Parser(queue, pattern)
        worker.start()
        workers.append(worker)
    return workers


def reader(filename, pattern, proccess):
    """
    Read file and separating by chromosome
    :param filename: filename with path: str
    :param pattern: search pattern: str
    :param proccess: number of proccess: int
    :return:
    """
    q = Queue()
    workers = build_worker_pool(q, proccess, pattern)
    main_line = []

    with open(filename, 'r') as f:
        for line in f:
            if line.startswith('>chr'):
                chromosome = line[1:].rstrip()

                if len(main_line) > 0:
                    q.put({
                        'line': ''.join(main_line),
                        'out': chromosome
                    })

                    main_line = []
                continue

            if not line.startswith(';'):
                main_line.append(line[:-2].upper())

    for _ in workers:
        q.put('quit')
    for worker in workers:
        worker.join()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument('-f', '--file',
    #                     help='Genome filename with path',
    #                     required=True)
    # parser.add_argument('-s', '--search',
    #                     help='search pattern',
    #                     required=True)
    # parser.add_argument('-p', '--proccess',
    #                     help='Number of proccess. By default - 4',
    #                     default=4,
    #                     type=int)
    # args = parser.parse_args()

    start = datetime.now()
    # search = args.search.upper()
    search = 'AANGGA'
    # proccess = args.proccess
    proccess = 4
    # file = args.file
    file = 'C:\genome.fa'

    pattern = genereate_rgex(search)
    print(pattern)
    reader(file, pattern, proccess)

    print('End {}'.format(str(datetime.now() - start)))
