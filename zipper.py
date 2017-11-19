import zipfile
import subprocess

command = ['scripts/cluster/cluster_metrics_grepsr.py', '/scripts/cluster/Drones - 3034 Companies.csv', '/scripts/cluster/Drones.json', 'cluster_adjacency_tightness_score.zip']
p = subprocess.Popen(command)
p.wait()

print("zipping")
