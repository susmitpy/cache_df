# Cache Pandas Dataframes to Disk

Easily cache Pandas Dataframes to disk using a simple interface.

## Sample usage


```python
from cache_df import CacheDF
import pandas as pd

cache = CacheDF(cache_dir='./caches')

# Caching a dataframe
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
cache.cache(df, 'my_df')

# Checking if a dataframe is cached
df_is_cached = cache.is_cached('my_df')

# Reading a dataframe from cache
try:
    df = cache.read('my_df')
    df_selective_cols = cache.read('my_df', cols=['a'])  # Read only a subset of columns
except FileNotFoundError:
    print('Dataframe not cached')

# Deleting a dataframe from cache if it exists
cache.uncache('my_df')

# Clearing all cached dataframes
cache.clear()
```

## Where it can be used
1) It can be used when you are using a shared file system across multiple machines such as AWS EFS, GCP Filestore, Azure Files, etc.



