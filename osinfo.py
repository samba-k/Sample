import yaml
h1 = ['virtual_memory']
h2 = ['Disk_partitions']
r = ['psutil.virtual_memory().total', 'psutil.virtual_memory().available', 'psutil.virtual_memory().percent', 'psutil.virtual_memory().used', 'psutil.virtual_memory().free']
r1 = [8465113088, 3024809984, 64.3, 5440303104, 3024809984]
r2 = ['psutil.disk_partitions().device()', 'psutil.disk_partitions().mountpoint()', 'psutil.disk_partitions().fstype()', 'psutil.disk_partitions().opts()', 'psutil.disk_partitions().maxfile()', 'psutil.disk_partitions().maxpath()']
r3 = ['C:\\', 'C:\\', 'NTFS', 'rw,fixed', '255', '260']
R1 = dict(zip(r,r1))
R2 = dict(zip(r2,r3))
result = {h1[0] : R1, h2[0] : R2}
with open ("test.yaml", 'w')as file:
    result1 = yaml.dump(result, file, default_flow_style=False)

