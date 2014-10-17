# coding: utf-8        

import subprocess
from itertools import izip, izip_longest

from wox import Wox,WoxAPI

class ZhenXiang(Wox):

    def query(self, key):
        key = key.strip()
        if not key:
            return []
        s = key.split(' ')
        fake, real = s[0], s[1:]
        f = izip_longest if len(fake) > len(real) else izip
        ans = ''.join('%s(%s)' % (x, y) if y else x for x, y in f(fake, real))
        return [{
            'Title': ans,
            'SubTitle': '按回车键复制结果至剪切板',
            'JsonRPCAction': {'method': 'copy', 'parameters': [ans]}
        }]

    def copy(self, text):
        command = 'echo ' + text.encode('gbk') + '| clip'
        subprocess.call(command, shell=True)

if __name__ == "__main__":
    ZhenXiang()