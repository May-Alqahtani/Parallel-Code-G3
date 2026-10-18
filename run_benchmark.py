import time
from Drain import LogParser

# 1. File Configuration
input_dir = './'
output_dir = './result/'
log_file = 'HDFS_large.log'

log_format = '<Date> <Time> <Pid> <Level> <Component>: <Content>'
regex = [r'blk_(|-)\d+', r'(\d+\.){3}\d+']

print("--------------------------------------------------")
print("Starting log processing (Sequential Processing)...")
print("--------------------------------------------------")

start_time = time.time()

# 2. Run Algorithm
parser = LogParser(log_format, indir=input_dir, outdir=output_dir, depth=4, st=0.5, rex=regex)
parser.parse(log_file)

end_time = time.time()
execution_time = end_time - start_time

# 3. Calculate Minutes and Seconds
minutes = int(execution_time // 60)
seconds = execution_time % 60

print("--------------------------------------------------")
print("Processing completed successfully!")
print(f"Total Execution Time: {minutes} minutes and {seconds:.2f} seconds ({execution_time:.4f} total seconds)")
print("--------------------------------------------------")