#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
	du = shutil.disk_usage(disk)
	free = du.free /du.total * 100
	return free > 200


def cpu_usage_check():
	usage = psutil.cpu_percent(1)
	return usage < 75

if not check_disk_usage("/") or not cpu_usage_check():
	print("ERROR")
else:
	print("every thing is fine")