#load libraries
import pandas as pd
from tqdm import tqdm

input_file = 'archive/custom_1988_2020.csv'
output_file = 'new_file.csv'

#reading the file
chunk_size = 1000000

total_rows = sum(1 for _ in open(input_file, 'r'))

csv_reader = pd.read_csv(input_file, chunksize=chunk_size)

final_chunks = []

for chunk in tqdm(csv_reader, total=total_rows // chunk_size +1, desc="Reading"):
        first_column_name = chunk.columns[0]
        chunk[first_column_name] = 'Python' + chunk[first_column_name].astype(str)
        final_chunks.append(chunk)
final_data = pd.concat(final_chunks, ignore_index=True)

#writing the file
chunk_size_write = 500000
total_rows_write = len(final_data)

with tqdm(total=total_rows_write, desc="Writing") as pbar:
        for i in range(0, total_rows_write, chunk_size_write):
            final_data.iloc[i:i+chunk_size_write].to_csv(output_file, mode='a', index=False, header=(i==0))
            pbar.update(chunk_size_write)

print("Processing is complete")