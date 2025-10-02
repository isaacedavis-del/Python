from sys import path
path.append('c:\\Users\\idavis013\\OneDrive - pwc\\Documents\\Python\\PCAP\\Module 1\\modules')
path.append('c:\\Users\\idavis013\\OneDrive - pwc\\Documents\\Python\\PCAP\\Module 1\\packages')

from module import suml, prodl

zeroes = [0 for _ in range(5)]
ones = [1 for _ in range(5)]
print(suml(zeroes))
print(prodl(ones))

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())
