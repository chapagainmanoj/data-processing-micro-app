"""

Author: HB Boosalis
September 21, 2017

Description:
Takes a network JSON and calculates ther intercluster strength and cluster
tightness for each cluster and for each clustering granularity.
Requires a CSV file of the network as well.

The command:
$ python cluster_metrics_grepsr.py '/path/to/json/file' '/path/to/csv/file'

Outputs up to 6 files, 2 for each existing granularity:
	Cluster_Tightness_louvain_*.csv 			*0-2
	Intercluster_Strength_gran_louvain_*.csv 	*0-2

"""


import json
import csv
import sys

from collections import OrderedDict as OD


json_f = sys.argv[1]
csv_f = sys.argv[2]

with open(json_f, 'r') as f:
	data = json.load(f)
with open(csv_f, 'r') as f:
	reader = csv.DictReader(f)
	data2 = list(reader)

# Get number of granularities:
num_gran = len(data['clusteringData'])

for gran in range(num_gran):

	gran_name = data['clusteringData'][gran]['name']
	clusters_list = data['clusteringData'][gran]['communities']
	num_clusters = len(clusters_list)

	# Strength between pairwise clusters
	interclust_strength = {}

	# Cluster tightness
	clust_tightness = {}

	# Mapping between old and new cluster names
	clust_name = {}

	for c1 in range(num_clusters):
		c1_nodes = clusters_list[c1]['nodeIDs']
		intralinks = 0
		intralinks2 = 0

		# First we need to map old cluster names (in the JSON) to the new
		# (in the CSV). Check that three nodes in c1_nodes have the same
		# new cluster name
		new_name = set()
		cnt = 0
		for row in data2:
			if int(row['Node ID']) in c1_nodes:
				cnt += 1
				new_name |= { row['Clusters ' + str(gran)] }
				if cnt == 3: break

		if len(new_name) != 1:
			print "\nNode assignment to clusters not consistent between JSON and CSV."
			print "Please check that the two files are sourced from the same network. Exiting.\n\n"
			sys.exit()

		clust_name[clusters_list[c1]['name']] = list(new_name)[0]

		# Intercluster strength
		for c2 in [c2 for c2 in range(num_clusters) if c2 > c1]:
			c2_nodes = clusters_list[c2]['nodeIDs']
			interlinks = 0
			for link in data['linkData']:
				if (link['source'] in c1_nodes and link['target'] in c2_nodes) \
				or (link['source'] in c2_nodes and link['target'] in c1_nodes):
					interlinks += 1
			interclust_strength[str(c1)+'|'+str(c2)] \
				= float(interlinks) / len(c1_nodes) / len(c2_nodes)

		# Cluster tightness
		for link in data['linkData']:
			if link['source'] in c1_nodes and link['target'] in c1_nodes:
				intralinks += 1
		clust_tightness[c1] = float(intralinks) / len(c1_nodes)


	interclust_data = []
	interclust_strength = OD(sorted(interclust_strength.items(), key=lambda t:t[1], reverse=True))
	for pair, ics in interclust_strength.items():
		c1 = int(pair.split('|')[0])
		c2 = int(pair.split('|')[1])
		cluster1 = clust_name[clusters_list[c1]['name']]
		cluster2 = clust_name[clusters_list[c2]['name']]

		row = {}
		if ics > 0.0:
			row['Cluster 1'] = cluster1
			row['Cluster 2'] = cluster2
			row['Intercluster Strength'] = ics
			interclust_data.append(row)

	keys = ['Cluster 1', 'Cluster 2', 'Intercluster Strength']

	with open('Cluster_Adjacency_Score_gran_%s.csv' % gran_name, 'w') as f:
		writer = csv.DictWriter(f, keys)
		writer.writeheader()
		writer.writerows(interclust_data)

	clust_data = []
	clust_tightness = OD(sorted(clust_tightness.items(), key=lambda t:t[1], reverse=True))
	for c1, ct in clust_tightness.items():
		cluster1 = clusters_list[c1]['name']
		row = {}
		row['Cluster'] = clust_name[clusters_list[c1]['name']]
		row['Cluster Tightness'] = ct
		row['Node Count'] = len(clusters_list[c1]['nodeIDs'])
		row['Quid Cluster ID'] = clusters_list[c1]['id']
		clust_data.append(row)

	keys = ['Cluster', 'Cluster Tightness', 'Node Count', 'Quid Cluster ID']

	with open('Cluster_Tightness_%s.csv' % gran_name, 'w') as f:
		writer = csv.DictWriter(f, keys)
		writer.writeheader()
		writer.writerows(clust_data)
