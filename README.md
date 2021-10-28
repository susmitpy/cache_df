# Cache Pandas Dataframe to Disk

Easily cache Pandas Dataframes to disk using a simple interface.

## Sample usage


```python
import CacheDF
import pandas as pd

cache_df = CacheDF(cache_dir='./caches')

# Caching a dataframe
df = pd.DataFrame(...)
cache_df.cache(df, 'my_df')

# Checking if a dataframe is cached
df_is_cached = cache_df.is_cached('my_df')

# Reading a dataframe from cache
try:
    df = cache_df.read('my_df')
except FileNotFoundError:
    print('Dataframe not cached')

# Deleting a dataframe from cache if it exists
cache_df.uncache('my_df')

# Clearing all cached dataframes
cache_df.clear()
```

## Where it can be used
1) It can be used when you are using a shared file system across multiple machines such as AWS EFS, GCP Filestore, Azure Files, etc.



