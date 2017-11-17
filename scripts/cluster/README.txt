2017-09-21

README for cluster_metrics_grepsr.py


Description:
Takes a network JSON and calculates ther intercluster strength and cluster
tightness for each cluster and for each clustering granularity.
Requires a CSV file of the network as well.

The command:
$ python cluster_metrics_grepsr.py '/path/to/json/file' '/path/to/csv/file'

Outputs up to 6 files, 2 for each existing granularity:
	Cluster_Tightness_louvain_*.csv                 *0-2
	Intercluster_Strength_gran_louvain_*.csv        *0-2
