# Clustering

1. Algorithm
2. By-hand Demo?
3. sklearn demo
4. Visualize results
    - gotcha w/ seaborn
5. Elbow method for choosing # of clusters

```python
import kmeans_lesson_util

kmeans_lesson_util.viz_initial()

kmeans_lesson_util.viz_initial(True)

kmeans_lesson_util.assign_clusters()
kmeans_lesson_util.viz()

kmeans_lesson_util.update_centroids()
kmeans_lesson_util.viz()

kmeans_lesson_util.assign_clusters()
kmeans_lesson_util.viz()

# etc...
```
