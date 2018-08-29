"""
How to get the datasets that come with scikit-learn package?
"""

from sklearn import datasets
#If we want some specific data set we can import the same.
iris = datasets.load_iris()

"""
Give example of two datasets that is shipped with scikit-learn package. Show example
how to use one. 
"""
iris = datasets.load_iris()  #This is Iris Data set
datasets.load_boston(return_X_y=False) #This is the all famous Boston House Price Problem.

"""
List at least 5 modules from scikit-learn?

1. Clustering --- this is for UnSupervised Learning
2. Cross Validation
3. Datasets -- mentioned in above problems.
4. Dimensionality Reduction 
5. Feature Extraction
6. Feature Selection
7. Supervised Models

"""

"""
Take input as few random points in a two dimensional space and divide them into 4
clusters. 
"""
import matplotlib.pyplot as plt
from sklearn.cluster import MiniBatchKMeans, KMeans
from sklearn.datasets.samples_generator import make_blobs
import numpy as np

##############################################################################
# Generate sample data
np.random.seed(0)
customPalette = ['#630C3A', '#39C8C6', '#D3500C', '#FFB139']

batch_size = 45
centers = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
n_clusters = len(centers)
X, labels_true = make_blobs(n_samples=30, centers=centers, cluster_std=0.7)

##############################################################################
# Compute clustering with Means

k_means = KMeans(init='k-means++', n_clusters=4, n_init=10)
k_means.fit(X)

##############################################################################
# Plot the results
for i in set(k_means.labels_):
    index = k_means.labels_ == i
    plt.plot(X[index,0], X[index,1], 'o')

#plt.show()


"""
Use K-means algorithm by using Scikit-learn to find the centroids of each cluster
"""
#############################################################################
#Finding Centroid
centroids = {'A': k_means.cluster_centers_[0],
          'B': k_means.cluster_centers_[1],
          'C': k_means.cluster_centers_[2],
          'D': k_means.cluster_centers_[3]}
print("Centroids: ", centroids)

"""
Plot the points along with the centroids. To distinguish the centroids, use some
special symbols like ‘+’ or ‘#’ etc.
"""
#Basically we need to annotate these centroids with specific symbols

for i, label in enumerate(centroids.keys()):
    plt.annotate(label,
                 centroids[label],
                 horizontalalignment='center',
                 verticalalignment='center',
                 size=20, weight='bold',
                 color=customPalette[i])

plt.show()

"""
How many daemon processes run on a Hadoop cluster? Explain.
==================================================================================================================================================================================================================================

NameNode- It is also known as Master in Hadoop cluster. It stores meta-data i.e. number of Blocks, their location, replicas and other details. 
          NameNode maintains and manages the slave nodes, and assigns tasks to them. It should be deployed on reliable hardware as it is the centerpiece of HDFS.
          
Secondary NameNode- It download the FsImage and EditLogs from the NameNode. Then it merges EditLogs with the Fsimage periodically. 
                    It keeps edits log size within a limit. Then it store the modified FsImage into persistent storage. So we can use FsImage in case of NameNode failure.
                    
DataNode- It is also known as Slave node. It is responsible for storing actual data in HDFS. DataNode perform read and write operation as per request for the clients.

Node Manager- It is the per-machine/per-node framework agent. It is responsible for containers, monitoring their resource usage and reporting the same to the Resource manager.

ResourceManager- The YARN Resource Manager Service (RM) is the central controlling authority for resource management and makes allocation decisions. ResourceManager has two main components: Scheduler and ApplicationsManager.

==================================================================================================================================================================================================================================

If Hadoop spawned 200 tasks for a job and one of the task failed. What will Hadoop do in this case?
    It will restart the task again on some other TaskTracker and only if the task fails more than four (default setting and can be changed) times will it kill the job.

==================================================================================================================================================================================================================================
Where does mapper output store the intermediate results?
    It actually depends if you have any reducers for the given job. 
    
    Case No Reducers
    ----------------
        Then the output is stored in HDFS only as it will be the final output of the job 
     
    Case Reducers are there
    -----------------------
        The output of mappers are only intermediate outputs. 
        Since placing an intermediate output in HDFS (with replication factor) will be waste of HDFS space so it is stored in LOCAL FILE SYSTEM. And in this case, final output of reducer is placed in HDFS .

==================================================================================================================================================================================================================================
When does reducers start their execution in a map reduce process?
        
    As much I understand Reduce phase start with the map phase and keep consuming the record from maps. 
    However since there is sort and shuffle phase after the map phase all the outputs have to be sorted and sent to the reducer. 
    So logically you can imagine that reduce phase starts only after map phase but actually for performance reason reducers are also initialized with the mappers.

==================================================================================================================================================================================================================================

"""


