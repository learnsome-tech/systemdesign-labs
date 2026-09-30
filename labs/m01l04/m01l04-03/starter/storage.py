WRITES_A_DAY = 40_000_000
ROW_BYTES = 400
INDEX_FACTOR = 1.3
REPLICAS = 3
DAYS = 365
GB = 1000 ** 3

raw_day = WRITES_A_DAY * ROW_BYTES
raw_year = raw_day * DAYS
on_disk = raw_year * INDEX_FACTOR * REPLICAS
print(f"raw a day      {raw_day / GB:9.1f} GB")
print(f"raw a year     {raw_year / GB:9.1f} GB")
print(f"with indexes   {raw_year * INDEX_FACTOR / GB:9.1f} GB")
print(f"times {REPLICAS} copies {on_disk / GB:9.1f} GB")
for shards in (4, 8, 16):
    print(f"{shards:>3} shards -> {on_disk / GB / shards:8.1f} GB each")
