import psutil
import json

r = ['psutil.cpu_times().user()', 'psutil.cpu_times().system()', 'psutil.cpu_times().idle()', 'psutil.cpu_times().interrupt', 'psutil.cpu_times().dpc()']
r1 = [1034.4375,1007.5625, 3047.71875, 14.421875, 25.140625]
r3 = ['psutil.cpu_percent(1)']
r4 = [5.1]
r5 = ['psutil.cpu_count()']
r6 = [4]
r7 = ['psutil.cpu_stats().ctx_switches()', 'psutil.cpu_stats().interrupts()', 'psutil.cpu_stats().soft_interrupts()', 'psutil.cpu_stats().syscalls()']
r8 = [18297691, 9733345, 0, 103080018]
r9 = ['psutil.cpu_freq().current', 'psutil.cpu_freq().max', 'psutil.cpu_freq().min']
r10 = [1700.0, 0.0, 2401.0]
r11 = ['psutil.getloadavg()']
r12 = [0.0, 0.0, 0.0]
r13 = ['psutil.virtual_memory().total()', 'psutil.virtual_memory().available()', 'psutil.virtual_memory().percent()', 'psutil.virtual_memory().used()', 'psutil.virtual_memory().free()']
r14 = [8465113088, 3024809984, 64.3, 5440303104, 3024809984]
r15 = ['psutil.swap_memory().total()', 'psutil.swap_memory().used()', 'psutil.swap_memory().free()', 'psutil.swap_memory().percent()', 'psutil.swap_memory().sin()', 'psutil.swap_memory().sout()']
r16 = [1342177280, 79314944,1262862336, 5.9, 0, 0]
r17 = ['psutil.disk_partitions().device()', 'psutil.disk_partitions().mountpoint()', 'psutil.disk_partitions().fstype()', 'psutil.disk_partitions().opts()', 'psutil.disk_partitions().maxfile()', 'psutil.disk_partitions().maxpath()']
r18 = ['C:\\', 'C:\\', 'NTFS', 'rw,fixed', '255', '260']
r19 = ['psutil.disk_usage().total()', 'psutil.disk_usage().used()', 'psutil.disk_usage().free()', 'psutil.disk_usage().percent()']
r20 = [479437840384, 99668447232, 379769393152, 20.8] 
r21 = ['psutil.net_io_counters().bytes_sent()', 'psutil.net_io_counters().bytes_recv()', 'psutil.net_io_counters().packets_sent()', 'psutil.net_io_counters().packets_recv()', 'psutil.net_io_counters().errin()', 'psutil.net_io_counters().errout()', 'psutil.net_io_counters().dropin()', 'psutil.net_io_counters().dropout()']
r22 = [20979491, 213371900, 88206, 181372, 0, 0, 0, 0]
r23 = ['psutil.sensors_battery().percent()', 'psutil.sensors_battery().secsleft()', 'psutil.sensors_battery().power_plugged()']  
r24 = [45, 3517, 'False']
r25 = ['psutil.boot_time()']   
r26 = [1718481673.6176705]
r27 = ['psutil.users().name()', 'psutil.users().terminal()', 'psutil.users().host()', 'psutil.users().started()', 'psutil.users().pid()']
r28 = ['owner', 'None', 'None', 1718481730.1500585, 'None']
R = dict(zip(r,r1))
R1 = dict(zip(r3,r4))
R2 = dict(zip(r5,r6))
R3 = dict(zip(r7,r8))
R4 = dict(zip(r9,r10))
R5 = dict(zip(r11,r12))
R6 = dict(zip(r13,r14))
R7 = dict(zip(r15,r16))
R8 = dict(zip(r17,r18))
R9 = dict(zip(r19,r20))
R10 = dict(zip(r21,r22))
R11 = dict(zip(r23,r24))
R12 = dict(zip(r25,r26))
R13 = dict(zip(r27,r28))
result = {**R, **R1, **R2, **R3, **R4, **R5, **R6, **R7, **R8, **R9, **R10, **R11, **R12, **R13}
result1 =json.dumps(result, indent=4)
file = open('ps.txt', 'w')
file.write(result1)

