#!/usr/bin/python
#coding=utf-8

import thread 
from time import sleep, ctime

loops = [4, 2]

def loop(nloop, nsec, lock):
	print 'Start loop ', nloop, 'at:', ctime()
	sleep(nsec)
	print 'loop ', nloop, 'done at:', ctime()
	
	# 解锁
	lock.release()
	
def main():
	print 'Start at:', ctime()
	locks = []
	
	nloops = range(len(loops))
	for i in nloops:
		lock = thread.allocate_lock()
		
		# 锁定
		lock.acquire()
		locks.append(lock)
	
	for i in nloops:
		thread.start_new_thread(loop, (i, loops[i], locks[i]))

	for i in nloops:
		while locks[i].locked():
			pass
			
	print 'all end:', ctime()
		
if __name__ == '__main__':
	main()