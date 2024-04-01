import os
from pathlib import Path

CURRENT_DIR = os.getcwd()

local_parquet = f"{CURRENT_DIR}/include/dataset/2024-03-31/parquet/"

print(local_parquet)