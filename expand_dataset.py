# كود لمضاعفة أسطر ملف HDFS ليصبح بحجم ضخم
input_file = 'HDFS_2k.log'
output_file = 'HDFS_large.log'

multiplier = 4500

print("Generating large dataset...")
with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

with open(output_file, 'w', encoding='utf-8') as f:
    for _ in range(multiplier):
        f.write(content)

print(f"Done! Created '{output_file}' with {2000 * multiplier} lines.")