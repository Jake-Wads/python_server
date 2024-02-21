# Spark Overview

1. Lessons -- Overview, Env Setup, Spark API, Wrangle, Explore
1. When would I use spark? When it is already setup for some reason or another
    - Big Data: velocity, volume, variety, veracity
        - Velocity: it is gathered quickly; streams
        - Volume: there's a lot of it; can require multi-computer clusters,
          bigger than memory
        - Variety: it's not uniform (not clean); can come from different sources
        - Veracity: might not be reliable (missing data)
    - when data is too big for memory (or storage)
    - distributed data (usually also too big)
    - streaming processing
    - alternatives: dask
1. Architecture
    - scala on JVM
    - client libraries talk to a running spark instance (e.g. pyspark)
        - all ends up as the same spark code
        - spark SQL
    - Driver(you/teammates) -- Cloud { Cluster Manager(1) -- Executors(many) }
        - viz 1
    - Application -> Job(1+) -> Task(1+)
    - Local Mode: everything on one machine; not so common in practice, but good
      if data fits in storage but not memory
        - viz 2
1. Parallel work
    - faster at scale, but some upfront overhead
        - e.g. webscraping pages across the class
    - two levels: executors and partitions
1. Spark Dataframes
    - abstracts everything above
    - like a pandas dataframe
    - lazy! doesn't do work until it has to
        - can be efficient, e.g. re-ordering operations
        - e.g. (map, filter) -> (filter, map)
    - **transformations** and **actions**
        - actions start a job, transformations don't
    - shuffle: avoid this when you can, biggest performance consideration
        - filter, map
        - sort, groupby


