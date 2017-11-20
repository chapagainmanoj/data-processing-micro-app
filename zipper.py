import zipfile
import subprocess

command = ['scripts/cluster/cluster_metrics_grepsr.py', 'scripts/cluster/Drones.json', 'scripts/cluster/Drones_Companies.csv', 'cluster_adjacency_tightness_score.zip']

# p = subprocess.Popen(command)
# p.wait()
subprocess.run(command)

print("zipping")
